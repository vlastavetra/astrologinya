import os
import sys
from pathlib import Path
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.responses import RedirectResponse

sys.path.append(Path(__file__).parents[1].as_posix())

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


@app.on_event("startup")
async def startup_event():
    from app.routes.forecast import forecast_routes

    app.include_router(forecast_routes, prefix="/api/v1/forecast", tags=["forecast"])


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", host="127.0.0.1", port=8003, log_level="info", reload=True
    )
