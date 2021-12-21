from fastapi import FastAPI
from app.api.routes import router as api_router


def get_application():
    app = FastAPI(title="ImageValidator", version="1.0.0")
    app.include_router(api_router, prefix="/api")

    return app


app = get_application()
