from fastapi import FastAPI
from application.adapters.order_service_adapter import OrderServiceAdapter
from domain.models import Order
from repositories.order_repository_impl import OrderRepositoryImpl
from schemas.order_schemas import OrderCreateSchema

app = FastAPI()

# Configure a instância do repositório
order_repository = OrderRepositoryImpl()

# Configure a instância do serviço de pedidos
order_service = OrderServiceAdapter(order_repository)


@app.post("/orders/", response_model=Order)
async def create_order(order_create: OrderCreateSchema):
    return order_service.create_order(order_create.customer_name, order_create.total_amount)


@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
    return order_service.get_order(order_id)
