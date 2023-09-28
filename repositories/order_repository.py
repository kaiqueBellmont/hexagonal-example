# repositories/order_repository.py
from abc import ABC, abstractmethod
from typing import List

from domain.models import Order


class OrderRepository(ABC):
    @abstractmethod
    def create_order(self, customer_name: str, total_amount: float) -> Order:
        pass

    @abstractmethod
    def get_orders(self) -> List[Order]:
        pass

    @abstractmethod
    def get_order(self, order_id: int) -> Order:
        pass


    def order_exists(self, order_id):
        pass
