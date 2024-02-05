from typing import Sequence


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
