# import modules/packages
from fastapi import APIRouter

# router instance
router = APIRouter()

# endpoints
@router.get("/home")
async def home():
    return "Welcome home Dev"