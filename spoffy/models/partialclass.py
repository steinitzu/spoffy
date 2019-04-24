from typing import List  # type: ignore

import attr

from spoffy.models.compat import is_union, is_list


_ib_params = ["type"]


def _is_attrs_class(cl) -> bool:
    return getattr(cl, "__attrs_attrs__", None) is not None


def _nullable_field(
    field: attr.Attribute, nested=True, ignore_attrs=None
) -> attr.Attribute:
    if ignore_attrs and field.name in ignore_attrs:
        return attr.ib(default=field.default, type=field.type)
    field_type = field.type
    if nested:
        if _is_attrs_class(field_type):
            field_type = make_partial_class(field_type)
        elif field_type and not is_union(field_type) and is_list(field_type):
            elem_type = field_type
            type_args = getattr(field_type, "__args__", ())
            if type_args:
                elem_type = type_args[0]
                if _is_attrs_class(elem_type):
                    elem_type = make_partial_class(elem_type)
                    field_type = List[elem_type]  # type: ignore

    return attr.ib(default=None, type=field_type)


def make_partial_class(cls, nested=True, ignore_attrs=None):
    return attr.make_class(
        cls.__name__ + "Partial",
        {
            f.name: _nullable_field(
                f, nested=nested, ignore_attrs=ignore_attrs
            )
            for f in attr.fields(cls)
        },
        bases=(cls,),
        kw_only=True,
    )
