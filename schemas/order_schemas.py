# order_schemas.py
from pydantic import BaseModel, field_validator


class OrderCreateSchema(BaseModel):
    customer_name: str
    total_amount: float

    @field_validator("customer_name")
    def validate_customer_name(cls, value: str):
        if len(value) < 4:
            raise ValueError("O nome deve ter pelo menos 4 caracteres.")
        return value


class OrderItem(BaseModel):
    product_name: str
    quantity: int
    price_per_unit: float

    @property
    def total_amount(self) -> float:
        return self.quantity * self.price_per_unit
