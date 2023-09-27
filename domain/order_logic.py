# domain/order_logic.py

from domain.models import Order
from typing import List


class OrderLogic:
    def calculate_total_amount(self, orders: List[Order]) -> float:
        total = sum(order.total_amount for order in orders)
        return total
