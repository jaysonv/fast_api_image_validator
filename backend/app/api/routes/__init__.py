from fastapi import APIRouter

from app.api.routes.cleanings import router as cleanings_router

from app.api.routes.isvalid import router as isvalid_router


router = APIRouter()


router.include_router(cleanings_router, prefix="/cleanings", tags=["cleanings"])

router.include_router(isvalid_router, prefix="/isvalid", tags=["valid"])
