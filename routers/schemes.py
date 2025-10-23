from fastapi import APIRouter
from services.farmer_schemes_service import get_farm_schemes

router = APIRouter(prefix="/schemes", tags=["Government Schemes"])

@router.get("/")
def list_farmer_schemes():
    return get_farm_schemes()
