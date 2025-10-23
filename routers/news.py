from fastapi import APIRouter
from services.news_service import get_agriculture_news

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/agriculture")
def fetch_agriculture_news():
    """
    Endpoint to get the latest agriculture news in India.
    """
    try:
        news = get_agriculture_news()
        return {"status": "success", "count": len(news), "data": news}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# usage    -    http://127.0.0.1:8000/news/agriculture