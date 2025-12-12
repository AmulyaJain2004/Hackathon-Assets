import joblib
import numpy as np

class ModelService:
    def __init__(self):
        self.model = joblib.load("models/model.pkl")

    def predict(self, data):
        features = np.array([[data.feature1, data.feature2]])
        prediction = self.model.predict(features)[0]
        return float(prediction)
