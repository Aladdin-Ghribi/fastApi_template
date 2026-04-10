from app.api.v1.routers.health import router as health_router #noqa: I001
from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router)
