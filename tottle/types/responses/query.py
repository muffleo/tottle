from typing import Optional

from pydantic import BaseModel, Field

from tottle.types.responses.chat import Message
from tottle.types.responses.location import Location
from tottle.types.responses.order import ShippingAddress, OrderInfo
from tottle.types.responses.user import User


class CallbackQuery(BaseModel):
    id: str
    sender: User = Field(alias="from")
    message: Optional["Message"] = None
    inline_message_id: Optional[str] = None

    chat_instance: str
    data: Optional[str] = None
    game_short_name: Optional[str] = None


class InlineQuery(BaseModel):
    id: str
    sender: User = Field(alias="from")
    location: Optional[Location] = None

    query: str
    offset: str


class ShippingQuery(BaseModel):
    id: str
    sender: User = Field(alias="from")
    invoice_payload: str
    shipping_address: ShippingAddress


class PreCheckoutQuery(BaseModel):
    id: str
    sender: User = Field(alias="from")

    currency: str
    total_amount: int

    invoice_payload: str
    shipping_option_id: Optional[str] = None
    order_info: Optional[OrderInfo] = None


class ChosenInlineResult(BaseModel):
    id: str = Field(alias="result_id")
    chooser: User = Field(alias="from")
    location: Optional[Location] = None

    inline_message_id: Optional[str] = None
    query: str
