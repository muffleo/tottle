from typing import Optional

from pydantic import BaseModel, Field

from ..responses.chat import Message
from ..responses.poll import Poll, PollAnswer
from ..responses.query import (
    InlineQuery,
    ChosenInlineResult,
    CallbackQuery,
    ShippingQuery,
    PreCheckoutQuery,
)


class Update(BaseModel):
    id: int = Field(alias="update_id")

    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None

    inline_query: Optional[InlineQuery] = None
    chosen_inline_result: Optional[ChosenInlineResult] = None

    callback_query: Optional[CallbackQuery] = None
    shipping_query: Optional[ShippingQuery] = None
    pre_checkout_query: Optional[PreCheckoutQuery] = None

    poll: Optional[Poll] = None
    poll_answer: Optional[PollAnswer] = None
