import typing

if typing.TYPE_CHECKING:
    from tottle.api import ABCAPI


class Base:
    def __init__(self, api: "ABCAPI") -> None:
        self.api = api

    @classmethod
    def get_set_params(cls, params: dict) -> dict:
        exclude_params = params.copy()
        exclude_params.update(params["kwargs"])
        exclude_params.pop("kwargs")
        return {
            k if not k.endswith("_") else k[:-1]: v
            for k, v in exclude_params.items()
            if k != "self" and v is not None
        }

    @classmethod
    def construct_api(cls, api: "ABCAPI") -> "Base":
        cls.api = api
        return cls
