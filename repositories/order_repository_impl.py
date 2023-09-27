#  Implementação do Repositório Concreto
# repositories/order_repository_impl.py
from domain.models import Order
from .order_repository import OrderRepository
from adapters.database_adapter import SessionLocal, OrderDB


class OrderRepositoryImpl(OrderRepository):
    def create_order(self, customer_name: str, total_amount: float) -> Order:
        db_order = OrderDB(customer_name=customer_name, total_amount=total_amount)
        db = SessionLocal()
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        db.close()
        return Order(id=db_order.id, customer_name=db_order.customer_name, total_amount=db_order.total_amount)

    def get_order(self, order_id: int) -> Order:
        db = SessionLocal()
        db_order = db.query(OrderDB).filter(OrderDB.id == order_id).first()
        db.close()

        if db_order:
            return Order(id=db_order.id, customer_name=db_order.customer_name, total_amount=db_order.total_amount)
        else:
            return None

    def order_exists(self, order_id: int) -> bool:
        db = SessionLocal()
        db_order = db.query(OrderDB).filter(OrderDB.id == order_id).first()
        db.close()
        return db_order is not None
