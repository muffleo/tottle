from typing import Optional

from pydantic import BaseModel

from tottle.types.responses.order import OrderInfo


class SuccessfulPayment(BaseModel):
    currency: str
    total_amount: str
    invoice_payload: str
    shipping_option_id: Optional[str] = None
    order_info: Optional[OrderInfo] = None
