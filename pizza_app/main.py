from fastapi import FastAPI
from . routers import auth_routes , order_routes
from .model import models
from .database import db 
from fastapi_jwt_auth import AuthJWT
from .schemas.schema import Settings

# app instance
app = FastAPI()

get_db = db.get_db
models.Base.metadata.create_all(db.engine)


@app.get("/")
def index():
    return 'Hello World'

# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()





# register all routers
app.include_router(auth_routes.auth_router)
app.include_router(order_routes.order_router    )