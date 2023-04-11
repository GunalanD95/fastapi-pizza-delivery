from pydantic import BaseModel
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

        schema_example = {
            'example': {
                'username': 'Gunalan D',
                'email'   : 'gunalan.d.official@gmail.com',
                'password': 'xxxx',
                'is_staff':  False,
                'logged_in': False,
            }
        }

