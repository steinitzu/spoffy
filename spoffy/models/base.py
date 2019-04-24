import json
from pprint import pformat
from typing import Dict, Any, List

from cattr import Converter


class SpotifyObject:
    __spotify_object__ = True

    def __init__(self, **d: Dict[str, Any]) -> None:

        # type_hints = getattr(self.__class__, "__annotations__", {})
        self.__annos = getattr(self.__class__, "__annotations__", {})
        self.__attrs: List[str] = []
        for key, value in d.items():
            self.__attrs.append(key)
            if isinstance(value, dict):
                setattr(self, key, self.__convert_nested(key, value))
            elif isinstance(value, list) and value:
                if isinstance(value[0], dict):
                    setattr(self, key, self.__convert_nested_list(key, value))
                else:
                    setattr(self, key, value)
            else:
                setattr(self, key, value)

    def __convert_nested(self, key, value: dict):
        return converter.structure(value, self.__annos.get(key, SpotifyObject))

    def __convert_nested_list(self, key, value: List[dict]):
        return converter.structure(
            value, self.__annos.get(key, List[SpotifyObject])
        )

    def to_dict(self) -> Dict[str, Any]:
        result = {}
        for key in self.__attrs:
            value = getattr(self, key)
            if hasattr(value, "to_dict"):
                value = value.to_dict()
            elif isinstance(value, list) and value:
                dict_list = hasattr(value[0], "to_dict")
                if dict_list:
                    value = [item.to_dict() for item in value]
            result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)

    def __repr__(self):
        return "<{} ({})>".format(
            self.__class__.__name__, pformat(self.to_dict())
        )


def convert_spotobject(obj, cl):
    return cl(**obj)


def is_obj(cls):
    return getattr(cls, "__spotify_object__", False)


converter = Converter()
converter.register_structure_hook_func(is_obj, convert_spotobject)
# converter.register_structure_hook(SpotifyObject, convert_spotobject)
