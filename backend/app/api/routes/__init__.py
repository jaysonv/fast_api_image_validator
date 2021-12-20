from fastapi import APIRouter

from app.api.routes.isvalid import router as isvalid_router


router = APIRouter()

router.include_router(isvalid_router, prefix="/isvalid", tags=["valid"])
