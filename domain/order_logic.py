# domain/order_logic.py

from domain.models import Order
from typing import List


class OrderLogic:
    DISCOUNT = 0.05

    def calculate_total_amount(self, orders: List[Order]) -> float:
        if any(order.total_amount == 0 for order in orders):
            for order in orders:
                if order.total_amount == 0:
                    order.total_amount = order.price_per_unit * order.quantity

            total_sum = sum(order.total_amount for order in orders)
            total_disc = total_sum - (total_sum * self.DISCOUNT)
            return round(total_disc, 2)
        else:
            # Se todos os `total_amount` já forem diferentes de zero, não há necessidade de recalcular
            total_sum = sum(order.total_amount for order in orders)
            total_disc = total_sum - (total_sum * self.DISCOUNT)
            return round(total_disc, 2)
