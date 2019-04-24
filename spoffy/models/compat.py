import sys
from typing import Sequence

version_info = sys.version_info[0:3]
is_py37 = version_info[:2] == (3, 7)

if is_py37:
    from typing import List, Union, _GenericAlias  # type: ignore

    def is_union(obj):
        return (
            obj is Union
            or isinstance(obj, _GenericAlias)
            and obj.__origin__ is Union
        )

    def is_list(type):
        return (
            type is List
            or type.__class__ is _GenericAlias
            and issubclass(type.__origin__, List)
        )

    def is_sequence(type):
        return (
            type is List
            or type.__class__ is _GenericAlias
            and issubclass(type.__origin__, Sequence)
        )


else:
    from typing import _Union, List  # type: ignore

    def is_union(obj):
        """Return true if the object is a union. """
        return isinstance(obj, _Union)

    def is_list(type):
        return issubclass(type, List)

    def is_sequence(type):
        return issubclass(type, Sequence)
