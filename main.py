# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("diabetes_model.pkl")

# data validation schema
# this allow the api to validate incoming data
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    BMI: float
    Age: int

@app.get("/")
def read_root():
    return {"message": "Diabetes Prediction API is live"}

@app.post("/predict")
def predict(data: DiabetesInput):
    input_data = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure, data.BMI, data.Age]])
    prediction = model.predict(input_data)[0]
    if prediction == 0:
        return {"diagnosis": "the person is not diabetic"}
    else:
        return {'diagnosis': "the person is diabetic"}
  
# to run the app, use the command:
# uvicorn main:app --reload