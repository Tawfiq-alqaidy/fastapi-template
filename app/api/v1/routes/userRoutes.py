from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from typing import List, Dict, Any # Import necessary types

route = APIRouter()

@route.get("/all", status_code=status.HTTP_200_OK)
async def get_users() -> JSONResponse: # Added return type hint
    """
    Get all users
    """
    # Corrected the structure to be a list of dictionaries
    # Removed incorrect semicolons
    users_data: List[Dict[str, Any]] = [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com", # Changed email for uniqueness
            "password": "password123",
            "created_at": "2023-10-01T12:00:00Z",
            "updated_at": "2023-10-01T12:00:00Z",
            "is_active": True,
            "is_superuser": False,
            "is_verified": True,
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "email": "jane.smith@example.com", # Changed email for uniqueness
            "password": "password123",
            "created_at": "2023-10-01T12:00:00Z",
            "updated_at": "2023-10-01T12:00:00Z",
            "is_active": True,
            "is_superuser": False,
            "is_verified": True,
        },
        {
            "id": 3,
            "name": "Alice Johnson",
            "email": "alice.johnson@example.com", # Changed email for uniqueness
            "password": "password123",
            "created_at": "2023-10-01T12:00:00Z",
            "updated_at": "2023-10-01T12:00:00Z",
            "is_active": True,
            "is_superuser": False,
            "is_verified": True,
        }
    ]
    return JSONResponse(content=users_data, status_code=status.HTTP_200_OK)
