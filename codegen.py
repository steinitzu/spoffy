from copy import deepcopy
from typing import Tuple, List

import black
import ast
import astor


source = open("spoffy/modules/sansio.py").read()
parsed = ast.parse(source)


def to_source(node) -> str:
    s = astor.to_source(node, pretty_source=lambda x: "".join(x))
    return s


def get_classes() -> List[ast.ClassDef]:
    return [
        node for node in ast.walk(parsed) if isinstance(node, ast.ClassDef)
    ]


def get_module_classes():
    return [
        c
        for c in get_classes()
        if c.bases and c.bases[0].id == "RequestBuilder"  # type: ignore
    ]


def get_class_methods(klass: ast.ClassDef) -> List[ast.FunctionDef]:
    return [
        node for node in ast.walk(klass) if isinstance(node, ast.FunctionDef)
    ]


def get_attributes(klass: ast.ClassDef) -> List[ast.Attribute]:
    return [
        node for node in ast.walk(klass) if isinstance(node, ast.Attribute)
    ]


def get_request_methods(klass: ast.ClassDef) -> List[ast.FunctionDef]:
    pass


def build_ret(method, rtype_arg):
    tmpl = (
        "return self._make_request(self.b.artist(artist_id=artist_id), Artist)"
    )
    ret = ast.parse(tmpl).body[0]

    ret.value.args[1] = rtype_arg  # type: ignore

    # TODO: Skip first arg (it's self)
    ret.value.args[0].args = []  # type: ignore
    ret.value.args[0].keywords = signature_to_keywords(method)  # type: ignore
    ret.value.args[0].func.attr = method.name  # type: ignore

    async_ret = deepcopy(ret)
    async_ret.value = ast.Await(ret.value)  # type: ignore
    return ret, async_ret


def signature_to_keywords(method):
    """
    Convert a method signature to
    keyword arguments ast objects
    """
    keywords = [
        ast.keyword(arg.arg, ast.Name(arg.arg, ast.Load()))
        for arg in method.args.args[1:]
    ]
    if method.args.kwarg:
        # Forward **kwargs to builder call if method has them
        kwarg_name = method.args.kwarg.arg
        keywords.append(  # type: ignore
            ast.keyword(None, ast.Name(kwarg_name, ast.Load()))
        )
    return keywords


def build_method_def(
    method: ast.FunctionDef,
) -> Tuple[ast.FunctionDef, ast.AsyncFunctionDef]:
    orig = method
    method = deepcopy(method)
    rtype_arg = method.decorator_list[0].args[0]  # type: ignore

    method.decorator_list = []
    method.returns = rtype_arg
    # method.returns.id = rtype  # type: ignore

    call, async_call = build_ret(method, rtype_arg)
    docstring = ast.get_docstring(orig)
    method.body = [call]
    if docstring:
        method.body.insert(0, orig.body[0])

    async_method = deepcopy(method)
    async_method = ast.AsyncFunctionDef(  # type: ignore
        **async_method.__dict__
    )
    async_method.body[-1] = async_call

    return method, async_method  # type: ignore


def add_mixins(name, klass: ast.ClassDef):
    mixintree = ast.parse(open("spoffy/modules/mixins.py").read())
    for node in mixintree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        if name + "Mixin" != node.name:
            continue
        klass.bases.append(
            ast.Attribute(
                ast.Name("mixins", ast.Load()), node.name, ast.Load()
            )
        )


def find_method(klass, name):
    for item in klass.body:
        if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if item.name == name:
            return item


def add_extras(klass: ast.ClassDef):
    if not klass.name.endswith("Auth"):
        return
    assign_methods = [
        (
            "authorize_user",
            "get_token_from_code",
            "token",
            _doc_authorize_user,
        ),
        (
            "authorize_client",
            "get_token_from_client_credentials",
            "token",
            _doc_authorize_client,
        ),
        (
            "refresh_authorization",
            "get_token_from_refresh_token",
            "token",
            _doc_refresh_authorization,
        ),
    ]
    tmpl = 'self._assign_result("token", self.method_name())'
    for methname, mirroredname, assignto, docstring in assign_methods:
        mirrored = find_method(klass, mirroredname)
        meth = deepcopy(mirrored)
        meth.name = methname
        keywords = signature_to_keywords(mirrored)
        assignment = ast.parse(tmpl).body[0]

        assignment.value.args[0].s = assignto  # type: ignore
        assignment.value.args[1].func.attr = mirrored.name  # type: ignore
        assignment.value.args[1].keywords = keywords  # type: ignore
        if isinstance(meth, ast.AsyncFunctionDef):
            assignment = ast.Expr(ast.Await(assignment.value))  # type: ignore

        body = [assignment]
        if docstring:
            docobj = ast.Expr(ast.Str(docstring))
            body.insert(0, docobj)

        meth.body = body
        meth.returns = None
        klass.body.append(meth)


def build_class(klass: ast.ClassDef) -> Tuple[ast.ClassDef, ast.ClassDef]:
    tmpl = "__builder_class__ = builders.Artists"
    klasscopy = deepcopy(klass)
    methods = [
        build_method_def(method) for method in get_class_methods(klasscopy)
    ]
    builder_class = ast.parse(tmpl).body[0]
    builder_class.value.attr = klass.name  # type: ignore
    klasscopy.body = [builder_class]  # type: ignore
    klasscopy.bases[0].id = "ApiModule"  # type: ignore

    async_class = deepcopy(klasscopy)
    async_class.name = "Async" + async_class.name
    async_class.bases[0].id = "AsyncApiModule"  # type: ignore

    sync_meths, async_meths = list(zip(*methods))
    klasscopy.body += sync_meths
    async_class.body += async_meths
    add_mixins(klasscopy.name, klasscopy)
    add_mixins(klasscopy.name, async_class)
    add_extras(klasscopy)
    add_extras(async_class)

    return klasscopy, async_class


def build_classes():
    new_body: List[ast.ClassDef] = []
    for klass in get_module_classes():
        new_body += list(build_class(klass))

    return new_body


_doc_authorize_client = """
        Authorize this API instance using
        its client ID and client Secret
        """

_doc_authorize_user = """
        Authorize this API instance using a response code
        from oauth login
        """

_doc_refresh_authorization = """
        :param refresh_token: Optional refresh token to use
            instead of the token stored on this instance
        """


if __name__ == "__main__":
    classes = build_classes()

    with open("spoffy/modules/modules.py", "r+") as output_file:
        out_source = output_file.read()
        output_file.seek(0)
        out_tree = ast.parse(out_source)
        out_body = [
            node
            for node in out_tree.body
            if isinstance(node, (ast.Import, ast.ImportFrom))
        ]
        out_body += classes
        out_tree = ast.Module(out_body)
        source = to_source(out_tree)
        source = black.format_str(source, mode=black.Mode(line_length=79))
        output_file.write(source)
        print(source)
