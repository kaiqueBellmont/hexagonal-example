from typing import List

from fastapi import FastAPI, HTTPException
from application.adapters.order_service_adapter import OrderServiceAdapter
from domain.models import Order
from repositories.order_repository_impl import OrderRepositoryImpl
from schemas.order_schemas import OrderCreateSchema, OrderItem
from domain.order_logic import OrderLogic

app = FastAPI()

# Configure a instância do repositório
order_repository = OrderRepositoryImpl()

# Configure a instância do serviço de pedidos
order_logic = OrderLogic()
order_service = OrderServiceAdapter(order_repository, order_logic)


@app.post("/orders/", response_model=Order)
async def create_order(order_create: OrderCreateSchema):
    return order_service.create_order(order_create.customer_name, order_create.total_amount)


@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
    if not order_service.order_exists(order_id):
        raise HTTPException(status_code=404, detail=f"A ordem com o ID {order_id} não foi encontrada.")
    return order_service.get_order(order_id)


@app.post("/calculate-order-total/")
async def calculate_order_total(order_items: List[OrderItem]):
    total = order_service.calculate_order_total(order_items)  # Passe a lista de OrderItem
    return {"total_amount": total}

