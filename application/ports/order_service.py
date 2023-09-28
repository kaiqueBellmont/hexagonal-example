# application/ports/order_service.py
from abc import ABC, abstractmethod
from typing import List


class OrderServicePort(ABC):
    @abstractmethod
    def create_order(self, customer_name: str, total_amount: float):
        pass

    @abstractmethod
    def get_order(self, order_id: int):
        pass

    @abstractmethod
    def calculate_order_total(self, orders):
        pass

    @abstractmethod
    def get_orders(self):
        pass

    @abstractmethod
    def order_exists(self, order_id: int):
        pass
