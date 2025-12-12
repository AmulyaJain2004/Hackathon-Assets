from fastapi import FastAPI
from routers.predict import router as PredictRouter

app = FastAPI(
    title="AI Microservice",
    description="FastAPI service for ML/DL predictions",
    version="1.0.0"
)

app.include_router(PredictRouter, prefix="/api")

@app.get("/")
async def root():
    return {"message": "FastAPI ML service is running"}
