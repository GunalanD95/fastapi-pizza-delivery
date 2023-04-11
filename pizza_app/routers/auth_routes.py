from fastapi import APIRouter


auth_router = APIRouter(
    tags=['auth'],
)


@auth_router.get("/login")
async def login():
    return 'Login Sucessfull'