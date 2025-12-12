from pydantic import BaseModel

class PredictInput(BaseModel):
    feature1: float
    feature2: float
