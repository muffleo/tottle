import typing

from .base import Base
from ..responses import chat


class ChatCategory(Base):
    async def kick_member(
            self,
            chat_id: typing.Union[int, str],
            user_id: int,
            until_date: typing.Optional[int],
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "kickChatMember", params
        )

    async def unban_member(
            self,
            chat_id: typing.Union[int, str],
            user_id: int,
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "unbanChatMember", params
        )

    async def restrict_member(
            self,
            chat_id: typing.Union[int, str],
            user_id: int,
            permissions: dict,
            until_date: typing.Optional[int],
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "restrictChatMember", params
        )

    async def promote_member(
            self,
            chat_id: typing.Union[int, str],
            user_id: int,
            can_change_info: typing.Optional[bool] = None,
            can_post_messages: typing.Optional[bool] = None,
            can_edit_messages: typing.Optional[bool] = None,
            can_delete_messages: typing.Optional[bool] = None,
            can_invite_users: typing.Optional[bool] = None,
            can_restrict_users: typing.Optional[bool] = None,
            can_pin_messages: typing.Optional[bool] = None,
            can_promote_members: typing.Optional[bool] = None,
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "promoteChatMember", params
        )

    async def set_administrator_custom_title(
            self,
            chat_id: typing.Union[int, str],
            user_id: int,
            custom_title: str,
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "setChatAdministratorCustomTitle", params
        )

    async def set_permissions(
            self,
            chat_id: typing.Union[int, str],
            permissions: dict,
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "setChatPermissions", params
        )

    async def export_invite_link(
            self,
            chat_id: typing.Union[int, str],
            **kwargs
    ) -> str:
        params = self.get_set_params(locals())
        return await self.api.request(
            "exportChatInviteLink", params
        )

    async def set_title(
            self,
            chat_id: typing.Union[int, str],
            title: str,
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "setChatTitle", params
        )

    async def set_description(
            self,
            chat_id: typing.Union[int, str],
            description: typing.Optional[str] = None,
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "setChatDescription", params
        )

    async def pin_message(
            self,
            chat_id: typing.Union[int, str],
            message_id: int,
            disable_notification: typing.Optional[bool] = None,
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "pinChatMessage", params
        )

    async def unpin_message(
            self,
            chat_id: typing.Union[int, str],
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "unpinChatMessage", params
        )

    async def leave_chat(
            self,
            chat_id: typing.Union[int, str],
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "leaveChat", params
        )

    async def get_chat(
            self,
            chat_id: typing.Union[int, str],
            **kwargs
    ) -> chat.Chat:
        params = self.get_set_params(locals())
        return await self.api.request(
            "getChat", params
        )

    async def get_administrators(
            self,
            chat_id: typing.Union[int, str],
            **kwargs
    ) -> typing.List[chat.ChatMember]:
        params = self.get_set_params(locals())
        members = await self.api.request(
            "getChatAdministrators", params
        )
        return [chat.ChatMember(**member) for member in members]

    async def get_members_count(
            self,
            chat_id: typing.Union[int, str],
            **kwargs
    ) -> int:
        params = self.get_set_params(locals())
        return await self.api.request(
            "getChatMembersCount", params
        )

    async def get_member(
            self,
            chat_id: typing.Union[int, str],
            user_id: int,
            **kwargs
    ) -> chat.ChatMember:
        params = self.get_set_params(locals())
        return chat.ChatMember(
            **await self.api.request(
                "getChatMember", params
            )
        )

    async def set_sticker_set(
            self,
            chat_id: typing.Union[int, str],
            sticker_set_name: str,
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "setChatStickerSet", params
        )

    async def delete_sticker_set(
            self,
            chat_id: typing.Union[int, str],
            **kwargs
    ) -> bool:
        params = self.get_set_params(locals())
        return await self.api.request(
            "deleteChatStickerSet", params
        )
