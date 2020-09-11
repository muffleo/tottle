from .base import Base
from ..responses import user


class UserCategory(Base):
    async def get_me(self, **kwargs) -> user.User:
        params = self.get_set_params(locals())
        return user.User(
            **await self.api.request(
                "getMe", params
            )
        )
