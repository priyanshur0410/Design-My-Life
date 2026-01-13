from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Life Design Backend Service")

app.include_router(router)
