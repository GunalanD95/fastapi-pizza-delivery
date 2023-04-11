from fastapi import APIRouter


order_router = APIRouter(
    tags=['order'],
    prefix='/order',
)


@order_router.get("")
async def orders():
    return 'Orders'