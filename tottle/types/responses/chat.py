from typing import Optional, List
from pydantic import BaseModel, Field

from ..responses.animation import Animation
from ..responses.audio import Audio
from ..responses.contact import Contact
from ..responses.dice import Dice
from ..responses.entity import Entity
from ..responses.game import Game
from ..responses.invoice import Invoice
from ..responses.keyboard import InlineKeyboardMarkup
from ..responses.location import Location
from ..responses.passport import PassportData
from ..responses.payment import SuccessfulPayment
from ..responses.photo import PhotoSize
from ..responses.poll import Poll
from ..responses.sticker import Sticker
from ..responses.user import User
from ..responses.venue import Venue
from ..responses.video import Video, VideoNote


class ChatPhoto(BaseModel):
    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str


class ChatPermissions(BaseModel):
    can_send_messages: Optional[bool] = None
    can_send_media_messages: Optional[bool] = None
    can_send_polls: Optional[bool] = None
    can_send_other_messages: Optional[bool] = None
    can_add_web_page_previews: Optional[bool] = None
    can_change_info: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_pin_messages: Optional[bool] = None


class ChatMember(BaseModel):
    user: "User"
    status: str
    custom_title: Optional[str] = ""
    until_date: Optional[int] = ""

    can_be_edited: Optional[bool] = None
    can_post_messages: Optional[bool] = None
    can_edit_messages: Optional[bool] = None
    can_delete_messages: Optional[bool] = None
    can_restrict_members: Optional[bool] = None
    can_promote_members: Optional[bool] = None
    can_change_info: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    is_member: Optional[bool] = None
    can_send_messages: Optional[bool] = None
    can_send_media_messages: Optional[bool] = None
    can_send_polls: Optional[bool] = None
    can_send_other_messages: Optional[bool] = None
    can_add_web_page_previews: Optional[bool] = None


class Chat(BaseModel):
    id: int
    type: str
    title: Optional[str] = ""
    username: Optional[str] = ""
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""
    photo: Optional["ChatPhoto"] = None
    description: Optional[str] = ""
    invite_link: Optional[str] = ""
    pinned_message: Optional["Message"] = None

    permissions: Optional["ChatPermissions"] = None
    slow_mode_delay: Optional[int] = 0
    sticker_set_name: Optional[str] = ""
    can_set_sticker_set: Optional[bool] = None


class Message(BaseModel):
    chat: "Chat"
    date: int
    message_id: int
    sender: Optional["User"] = Field(alias="from")

    forward_from: Optional["User"] = None
    forward_from_chat: Optional["Chat"] = None
    forward_from_message_id: Optional[int] = 0
    forward_signature: Optional[str] = ""
    forward_sender_name: Optional[str] = ""
    forward_date: Optional[int] = 0

    reply_to_message: Optional["Message"] = None
    via_bot: Optional["User"] = None
    edit_date: Optional[int] = 0

    media_group_id: Optional[str] = ""
    author_signature: Optional[str] = ""
    text: Optional[str] = ""
    entities: Optional[List["Entity"]] = []
    animation: Optional["Animation"] = None

    audio: Optional["Audio"] = None
    photo: Optional[List["PhotoSize"]] = []
    sticker: Optional["Sticker"] = None
    video: Optional["Video"] = None
    video_note: Optional["VideoNote"] = None

    caption: Optional[str] = ""
    caption_entities: Optional[List["Entity"]] = []

    contact: Optional["Contact"] = None
    dice: Optional["Dice"] = None
    game: Optional["Game"] = None
    poll: Optional["Poll"] = None
    venue: Optional["Venue"] = None
    location: Optional["Location"] = None

    new_chat_members: Optional[List["User"]] = []
    new_chat_title: Optional[str] = ""
    new_chat_photo: Optional[List["PhotoSize"]] = []
    delete_chat_photo: Optional[bool] = None
    group_chat_created: Optional[bool] = None
    supergroup_chat_created: Optional[bool] = None
    channel_chat_created: Optional[bool] = None

    migrate_to_chat_id: Optional[int] = 0
    migrate_from_chat_id: Optional[int] = 0

    pinned_message: Optional["Message"] = None
    invoice: Optional["Invoice"] = None
    successful_payment: Optional["SuccessfulPayment"] = None

    connected_website: Optional[str] = ""

    passport_data: Optional["PassportData"] = None
    reply_markup: Optional["InlineKeyboardMarkup"] = None


Chat.update_forward_refs()
Message.update_forward_refs()
