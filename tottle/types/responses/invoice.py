from pydantic import BaseModel


class Invoice(BaseModel):
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int
