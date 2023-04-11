from fastapi import FastAPI
from . routers import auth_routes , order_routes



# app instance
app = FastAPI()


@app.get("/")
def index():
    return 'Hello World'



# register all routers
app.include_router(auth_routes.auth_router)
app.include_router(order_routes.order_router    )