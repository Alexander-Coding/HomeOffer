from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.api import api_router
from src.core import start_rabbitmq, stop_rabbitmq

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_rabbitmq()

    yield

    await stop_rabbitmq()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Error-Code"],
)

app.add_middleware(GZipMiddleware, minimum_size=50)

app.include_router(api_router)


@app.get("/health")
async def health():
    return {"status": "ok"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="HomeOffer - Тестовое задание API",
        version="0.0.1",
        description="API для тестового задания HomeOffer",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
