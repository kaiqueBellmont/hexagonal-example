# graphql_schemas.py

import strawberry


@strawberry.type
class Order:
    id: int
    customer_name: str
    total_amount: float


@strawberry.input
class OrderItem:
    product_name: str
    quantity: int
    price_per_unit: float
    total_amount: float
