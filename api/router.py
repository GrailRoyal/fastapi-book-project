from fastapi import APIRouter
from api.routes.books import router as books_router

router = APIRouter()

# Include the books router
router.include_router(books_router, prefix="/books", tags=["books"])
