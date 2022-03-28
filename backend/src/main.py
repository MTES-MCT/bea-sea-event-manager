from fastapi import FastAPI

from src.routes import default_router

app = FastAPI()

app.include_router(default_router, prefix="")
