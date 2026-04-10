from app.core.logging import configure_logging # noqa: I001
from app.core.settings import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router 

app = FastAPI(title=settings.APP_NAME)




configure_logging()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(api_router)