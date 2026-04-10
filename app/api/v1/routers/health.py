from app.core.settings import settings #noqa: I001
from fastapi import APIRouter,status

router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok", "env": settings.APP_ENV}
