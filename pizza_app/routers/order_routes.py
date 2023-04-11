from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..model import models
from ..database import db

order_router = APIRouter(
    tags=['order'],
    prefix='/order',
)


@order_router.get("/")
async def orders():
    return {'Orders'}