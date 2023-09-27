# order_schemas.py
from pydantic import BaseModel


class OrderCreateSchema(BaseModel):
    customer_name: str
    total_amount: float

