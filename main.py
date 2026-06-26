from fastapi import FastAPI

from db import Base, engine
from routers import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD")

app.include_router(router)