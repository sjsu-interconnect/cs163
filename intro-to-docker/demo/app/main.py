from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict

app = FastAPI()

class FeaturesIn(BaseModel):
    """Input model for features.
    Accepts 4 float features based on the dummy dataset."""
    feature1: float
    feature2: float
    feature3: float
    feature4: float

class PredictionOut(BaseModel):
    """Output model for prediction."""
    prediction: int

@app.get("/")
def home():
    return {"health_check": "ok"}

@app.post("/predict", response_model=PredictionOut)
def predict_endpoint(payload: FeaturesIn):
    features = [
        payload.feature1, 
        payload.feature2, 
        payload.feature3, 
        payload.feature4
    ]
    prediction_result = predict(features)
    return {"prediction": prediction_result}