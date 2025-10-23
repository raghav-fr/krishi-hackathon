from fastapi import FastAPI
from routers import disease, weather, news, rates, schemes

app = FastAPI(
    title="FarmAssist API",
    description="the whole backend for the deepshiva hackathon project...",
    version="1.0.0"
)

# Routers
app.include_router(weather.router)
app.include_router(news.router)
app.include_router(rates.router)
app.include_router(schemes.router)
app.include_router(disease.router)

@app.get("/")
def home():
    return {"message": "Welcome to FarmAssist API 🌾"}
