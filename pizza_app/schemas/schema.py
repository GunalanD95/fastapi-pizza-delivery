from pydantic import BaseModel , BaseSettings
from typing   import Optional

# User Creation Model
class SignupModel(BaseModel):
    username  : str
    email_id  : str
    password  : str
    is_staff  : Optional[bool] 
    logged_in : Optional[bool]


    # need to add this line since we are using sql alchemy , we need this to interact with the api
    class Config:
        orm_mode = True 


class Settings(BaseSettings):
    authjwt_secret_key : str  = 'abea4bf991655185737332e26b1eef7e0b85fd9fc62b20ccd671971f07a96bcf'
    authjwt_algorithm: str = "HS256"


class LoginModel(BaseModel):
    username : str 
    password : str


