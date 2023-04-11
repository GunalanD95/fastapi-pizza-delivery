from fastapi import APIRouter ,  Depends  , HTTPException
# importing the db connection
from ..database.db import  get_db
from sqlalchemy.orm import Session
from ..schemas.schema import SignupModel
from ..model import models
from ..repos import user 

auth_router = APIRouter(
    tags=['auth'],
)


@auth_router.post("/signup")
async def sign_up(request: SignupModel,db : Session = Depends(get_db)) :
    return user.create_user(request , db)