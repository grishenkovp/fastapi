from fastapi import APIRouter
from app.api.sales import router as sales_router
from app.api.auth import router as auth_router
from app.api.reports import router as reports_router

router = APIRouter()
router.include_router(sales_router)
router.include_router(auth_router)
router.include_router(reports_router)
