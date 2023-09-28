# application/adapters/graphql_adapter.py

import strawberry
from typing import List

from application.ports.graphql_service import OrderServicePort
from domain.order_logic import OrderLogic
from repositories.order_repository_impl import OrderRepositoryImpl
from schemas.graphql_schema import Order, OrderItem

order_repository = OrderRepositoryImpl()
order_logic = OrderLogic()


@strawberry.input
class OrderItemInput:
    product_name: str
    quantity: int
    price_per_unit: float


@strawberry.type
class Query(OrderServicePort):

    @strawberry.field
    async def orders(self, info) -> List[Order]:
        orders = order_repository.get_orders()
        return orders

    @strawberry.field
    async def order(self, info, orderId: int) -> Order:
        order = order_repository.get_order(orderId)
        return order


@strawberry.type
class Mutation(OrderServicePort):
    @strawberry.mutation
    async def create_order(self, info, customer_name: str, total_amount: float) -> Order:
        new_order = order_repository.create_order(customer_name, total_amount)
        return new_order

    @strawberry.mutation
    async def calculate_order_total(self, orders: List[OrderItem]) -> float:
        return order_logic.calculate_total_amount(orders)


schema = strawberry.Schema(query=Query, mutation=Mutation)
