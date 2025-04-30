from fastapi import APIRouter
from .v1.routes import userRoutes


endpoints_router = APIRouter()

# Include the v1 endpoints
endpoints_router.include_router(userRoutes.route, prefix="/user", tags=["user"])
