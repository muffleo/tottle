from pydantic import BaseModel, Field
from typing import Optional, List

from tottle.types.objects.animation import Animation
from tottle.types.objects.audio import Audio
from tottle.types.objects.chat import Chat
from tottle.types.objects.contact import Contact
from tottle.types.objects.dice import Dice
from tottle.types.objects.game import Game
from tottle.types.objects.invoice import Invoice
from tottle.types.objects.keyboard import InlineKeyboardMarkup
from tottle.types.objects.location import Location
from tottle.types.objects.passport import PassportData
from tottle.types.objects.payment import SuccessfulPayment
from tottle.types.objects.photo import PhotoSize
from tottle.types.objects.poll import Poll
from tottle.types.objects.sticker import Sticker
from tottle.types.objects.user import User
from tottle.types.objects.venue import Venue
from tottle.types.objects.video import Video, VideoNote


class MessageEntity(BaseModel):
    type: str
    offset: int
    length: int
    url: Optional[str] = ""
    user: Optional[User] = None
    language: Optional[str] = ""


class Message(BaseModel):
    chat: Chat
    date: int
    message_id: int
    sender: Optional[User] = Field(None, alias="from")

    forward_from: Optional[User] = None
    forward_from_chat: Optional[Chat] = None
    forward_from_message_id: int
    forward_signature: str
    forward_sender_name: str
    forward_date: Optional[int] = 0

    reply_message: Optional["Message"] = Field(None, alias="reply_to_message")
    via_bot: Optional[User] = None
    edit_date: Optional[int] = 0

    media_group_id: Optional[str] = ""
    author_signature: Optional[str] = ""
    text: Optional[str] = ""
    entities: Optional[List[MessageEntity]] = []
    animation: Optional[Animation]

    audio: Optional[Audio] = None
    photo: Optional[List[PhotoSize]] = []
    sticker: Optional[Sticker] = None
    video: Optional[Video] = None
    video_note: Optional[VideoNote] = None

    caption: Optional[str] = ""
    caption_entities: Optional[List[MessageEntity]] = []

    contact: Optional[Contact] = None
    dice: Optional[Dice] = None
    game: Optional[Game] = None
    poll: Optional[Poll] = None
    venue: Optional[Venue] = None
    location: Optional[Location] = None

    new_chat_members: Optional[List[User]] = []
    new_chat_title: Optional[str] = ""
    new_chat_photo: Optional[List[PhotoSize]] = []
    delete_chat_photo: Optional[bool] = None
    group_chat_created: Optional[bool] = None
    supergroup_chat_created: Optional[bool] = None
    channel_chat_created: Optional[bool] = None

    migrate_to_chat_id: Optional[int] = 0
    migrate_from_chat_id: Optional[int] = 0

    pinned_message: Optional["Message"] = None
    invoice: Optional[Invoice] = None
    successful_payment: Optional[SuccessfulPayment] = None

    connected_website: Optional[str] = ""

    passport_data: Optional[PassportData] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
