from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from tottle.api import ABCAPI


class Base:
    def __init__(self, api: "ABCAPI") -> None:
        self.api = api

    @classmethod
    def get_set_params(cls, params: dict) -> dict:
        return {
            k if not k.endswith("_") else k[:-1]: v
            for k, v in params.items()
            if k != "self" and v is not None
        }

    @classmethod
    def construct_api(cls, api: "ABCAPI") -> Type["Base"]:
        cls.api = api
        return cls
