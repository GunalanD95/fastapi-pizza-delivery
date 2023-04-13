from fastapi import APIRouter ,  Depends  
# importing the db connection
from ..database.db import  get_db
from sqlalchemy.orm import Session
from ..schemas.schema import SignupModel , LoginModel
from fastapi_jwt_auth import AuthJWT
from ..repos import user 


auth_router = APIRouter(
    tags=['auth'],
)


@auth_router.post("/signup",status_code= 201)
async def sign_up(request: SignupModel,db : Session = Depends(get_db)) :
    return user.create_user(request , db)


@auth_router.post("/login",status_code= 200)
async def login(request: LoginModel,Authorize: AuthJWT = Depends() ,db : Session = Depends(get_db)) :
    return user.login_user(request, Authorize , db)