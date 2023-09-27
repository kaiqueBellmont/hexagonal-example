# order_service_adapter.py
from domain.models import Order
from application.ports.order_service import OrderServicePort
from repositories.order_repository import OrderRepository


class OrderServiceAdapter(OrderServicePort):
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def create_order(self, customer_name: str, total_amount: float) -> Order:
        return self.order_repository.create_order(customer_name, total_amount)

    def get_order(self, order_id: int) -> Order:
        return self.order_repository.get_order(order_id)


