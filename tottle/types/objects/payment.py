from pydantic import BaseModel
from typing import Optional

from tottle.types.objects.order import OrderInfo


class SuccessfulPayment(BaseModel):
    currency: str
    total_amount: str
    invoice_payload: str
    shipping_option_id: Optional[str] = ""
    order_info: Optional[OrderInfo] = None
