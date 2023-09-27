# main.py
from fastapi import FastAPI
from application.adapters.order_service_adapter import OrderServiceAdapter
from domain.models import Order

app = FastAPI()
order_service = OrderServiceAdapter()


@app.post("/orders/", response_model=Order)
async def create_order(customer_name: str, total_amount: float):
    return order_service.create_order(customer_name, total_amount)


@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
    return order_service.get_order(order_id)
