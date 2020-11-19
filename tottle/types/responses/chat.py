from typing import Optional, List
from pydantic import BaseModel, Field

from tottle.types.responses.alert import ProximityAlertTriggered
from tottle.types.responses.animation import Animation
from tottle.types.responses.audio import Audio
from tottle.types.responses.contact import Contact
from tottle.types.responses.dice import Dice
from tottle.types.responses.entity import Entity
from tottle.types.responses.game import Game
from tottle.types.responses.invoice import Invoice
from tottle.types.responses.keyboard import InlineKeyboardMarkup
from tottle.types.responses.location import Location
from tottle.types.responses.passport import PassportData
from tottle.types.responses.payment import SuccessfulPayment
from tottle.types.responses.photo import PhotoSize
from tottle.types.responses.poll import Poll
from tottle.types.responses.sticker import Sticker
from tottle.types.responses.user import User
from tottle.types.responses.venue import Venue
from tottle.types.responses.video import Video, VideoNote


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
    custom_title: Optional[str] = None
    until_date: Optional[int] = None

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
    title: Optional[str] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    photo: Optional["ChatPhoto"] = None
    description: Optional[str] = None
    invite_link: Optional[str] = None
    pinned_message: Optional["Message"] = None

    permissions: Optional["ChatPermissions"] = None
    slow_mode_delay: Optional[int] = None
    sticker_set_name: Optional[str] = None
    can_set_sticker_set: Optional[bool] = None


class Message(BaseModel):
    chat: "Chat"
    date: int
    message_id: int
    sender: Optional["User"] = Field(alias="from")

    forward_from: Optional["User"] = None
    forward_from_chat: Optional["Chat"] = None
    forward_from_message_id: Optional[int] = None
    forward_signature: Optional[str] = None
    forward_sender_name: Optional[str] = None
    forward_date: Optional[int] = None

    reply_to_message: Optional["Message"] = None
    via_bot: Optional["User"] = None
    edit_date: Optional[int] = None

    media_group_id: Optional[str] = None
    author_signature: Optional[str] = None
    text: Optional[str] = None
    entities: Optional[List["Entity"]] = None
    animation: Optional["Animation"] = None

    audio: Optional["Audio"] = None
    photo: Optional[List["PhotoSize"]] = None
    sticker: Optional["Sticker"] = None
    video: Optional["Video"] = None
    video_note: Optional["VideoNote"] = None

    caption: Optional[str] = None
    caption_entities: Optional[List["Entity"]] = None

    contact: Optional["Contact"] = None
    dice: Optional["Dice"] = None
    game: Optional["Game"] = None
    poll: Optional["Poll"] = None
    venue: Optional["Venue"] = None
    location: Optional["Location"] = None

    new_chat_members: Optional[List["User"]] = None
    new_chat_title: Optional[str] = None
    new_chat_photo: Optional[List["PhotoSize"]] = None
    delete_chat_photo: Optional[bool] = None
    group_chat_created: Optional[bool] = None
    supergroup_chat_created: Optional[bool] = None
    channel_chat_created: Optional[bool] = None

    migrate_to_chat_id: Optional[int] = None
    migrate_from_chat_id: Optional[int] = None

    pinned_message: Optional["Message"] = None
    invoice: Optional["Invoice"] = None
    successful_payment: Optional["SuccessfulPayment"] = None

    connected_website: Optional[str] = None

    passport_data: Optional["PassportData"] = None
    proximity_alert_triggered: Optional["ProximityAlertTriggered"] = None
    reply_markup: Optional["InlineKeyboardMarkup"] = None


Chat.update_forward_refs()
Message.update_forward_refs()
