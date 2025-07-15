from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.routers import routers
import uvicorn

app = FastAPI(
    title="FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    contact={
        "name": "Support Team",
        "email": "support@example.com"
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in routers:
    try:
        app.include_router(router, prefix='/api/v1')
    except ImportError as e:
        print(f"Could not import router {router}: {e}")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="info", reload=True)