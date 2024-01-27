import os
import sys
from pathlib import Path
import uvicorn
import certifi
ca = certifi.where()

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware import Middleware
from starlette.responses import RedirectResponse
from app.dal.mongo import MongoDb
from app.forecast.forecast import ForcastCreator


sys.path.append(Path(__file__).parents[1].as_posix())

load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

MONGO_URL = os.getenv("MONGO_URL")
if MONGO_URL is None:
    raise ValueError("MONGO_URL is not set. Please set it in .env file.")

ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(middleware=middleware)
app.client = AsyncIOMotorClient(MONGO_URL, tlsCAFile=certifi.where())

@app.post("/natal", responses={200: {"content": {"application/json": {}}}})
async def get_natal_card(data: dict):
    n = ForcastCreator(data['date'].replace("-", "/"), data['time'], f"{data['city']}, {data['country']}",  data['language'])
    promt = n.calculate_natal()
    answer = n.generate_chat_response(OPEN_AI_API_KEY, promt)
    return answer

@app.get("/house", responses={200: {"content": {"application/json": {}}}})
async def get_house(data: dict):
    n = ForcastCreator(data['date'].replace("-", "/"), data['time'], f"{data['city']}, {data['country']}", data['language'])
    promt = n.calculate_house()
    answer = n.generate_chat_response(OPEN_AI_API_KEY, promt)
    return answer

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", host="127.0.0.1", port=8004, log_level="info", reload=True
    )
