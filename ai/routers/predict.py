from fastapi import APIRouter
from schemas.predict_schema import PredictInput
from services.model_service import ModelService

router = APIRouter(prefix="/predict", tags=["Prediction"])
model_service = ModelService()

@router.post("/")
async def predict(data: PredictInput):
    prediction = model_service.predict(data)
    return {"prediction": prediction}
