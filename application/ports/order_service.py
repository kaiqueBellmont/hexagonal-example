from abc import ABC, abstractmethod


class OrderServicePort(ABC):
    @abstractmethod
    def create_order(self, customer_name: str, total_amount: float):
        pass

    @abstractmethod
    def get_order(self, order_id: int):
        pass
