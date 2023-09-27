# repositories/order_repository.py
from abc import ABC, abstractmethod
from domain.models import Order


class OrderRepository(ABC):
    @abstractmethod
    def create_order(self, customer_name: str, total_amount: float) -> Order:
        pass

    @abstractmethod
    def get_order(self, order_id: int) -> Order:
        pass
