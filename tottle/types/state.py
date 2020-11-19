from enum import IntEnum
from typing import Tuple, Type

from pydantic import BaseModel


class BaseStateGroup(IntEnum):
    pass


class StatePeer(BaseModel):
    peer_id: int
    state: int

    def get_state_path(self) -> Tuple[Type[BaseStateGroup], BaseStateGroup]:
        return self.state.__class__, self.state

    def get_state_repr(self) -> str:
        state_group, index = self.get_state_path()
        return f"{state_group.__name__}_{index}"
