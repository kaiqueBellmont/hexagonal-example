# application/order_Service_adapter.py
from typing import List

from domain.models import Order
from application.ports.order_service import OrderServicePort
from repositories.order_repository import OrderRepository
from domain.order_logic import OrderLogic


class OrderServiceAdapter(OrderServicePort):
    def __init__(self, order_repository: OrderRepository, order_logic: OrderLogic):
        self.order_repository = order_repository
        self.order_logic = order_logic

    def create_order(self, customer_name: str, total_amount: float) -> Order:
        return self.order_repository.create_order(customer_name, total_amount)


    def get_orders(self) -> List[Order]:
        return self.order_repository.get_orders()

    def get_order(self, order_id: int) -> Order:
        return self.order_repository.get_order(order_id)

    def calculate_order_total(self, orders):
        return self.order_logic.calculate_total_amount(orders)

    def order_exists(self, order_id: int) -> bool:
        return self.order_repository.order_exists(order_id)
