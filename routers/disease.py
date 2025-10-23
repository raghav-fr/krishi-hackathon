from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.disease_service import get_disease_details

router = APIRouter(prefix="/disease", tags=["Plant Disease Info"])

class DiseaseRequest(BaseModel):
    disease_name: str

@router.post("/info")
async def disease_info(request: DiseaseRequest):
    """Return AI-generated plant disease info"""
    try:
        result = get_disease_details(request.disease_name)
        return {"disease": request.disease_name, "details": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# POST → http://127.0.0.1:8000/disease/info

# Body (JSON):
# {
#   "disease_name": "Late blight of potato"
# }