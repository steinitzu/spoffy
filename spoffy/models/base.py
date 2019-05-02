from pydantic import BaseModel, BaseConfig, Extra


class Cfg(BaseConfig):
    extra = Extra.allow


class CustomMeta(BaseModel.__class__):  # type:ignore
    def __new__(mcs, name, bases, namespace):
        ret = super().__new__(mcs, name, bases, namespace)
        for field in ret.__fields__.values():
            field.required = False
            field.prepare()
        return ret


class SpotifyObject(BaseModel, metaclass=CustomMeta):
    Config = Cfg

    def __init__(self, **data) -> None:
        super().__init__(**data)
        for field in self.__fields_set__:
            if field not in self.__fields__:
                value = getattr(self, field)
                if isinstance(value, dict):
                    setattr(self, field, SpotifyObject(**value))
                elif (
                    value
                    and isinstance(value, list)
                    and isinstance(value[0], dict)
                ):
                    setattr(self, field, [SpotifyObject(**v) for v in value])
