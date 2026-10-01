from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api import router
from backend.app.core import config
from backend.app.core import services


app = FastAPI(title="F1 lab")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5175",
        "http://127.0.0.1:5175",
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

settings = config.get_settings()
app.state.services = services.build_services(settings)

app.include_router(router.router, prefix="/api/v1")
