from fastapi import APIRouter
from .category import router as category_router
from .tag import router as tag_router

router = APIRouter(
    prefix='/admin',
)

router.include_router(category_router)
router.include_router(tag_router)
