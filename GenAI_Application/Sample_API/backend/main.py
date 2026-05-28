from fastapi import FastAPI
from routes.gemini import router

app = FastAPI()

app.include_router(router)