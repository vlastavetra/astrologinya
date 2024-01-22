from fastapi import APIRouter, HTTPException, Form

from app.main import app
from app.dal.mongo import MongoDb

forecast_routes = APIRouter()


@forecast_routes.get("/natal-card")
async def get_natal_card():
    """
    Get list of all indices from db
    """
    try:
        return await MongoDb(app.client).get_natal_card()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    