# application/ports/graphql_service.py

from abc import ABC, abstractmethod
from typing import List

from schemas.graphql_schema import Order
from schemas.order_schemas import OrderItem


class OrderServicePort(ABC):
    @abstractmethod
    def create_order(self, customer_name: str, total_amount: float) -> Order:
        pass

    @abstractmethod
    def order_exists(self, order_id: int) -> bool:
        pass

    @abstractmethod
    def get_order(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def get_orders(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def calculate_order_total(self, order_items: List[OrderItem]) -> float:
        pass
