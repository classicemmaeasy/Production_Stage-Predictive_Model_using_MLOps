# main.py
from fastapi import FastAPI,Request
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


model = joblib.load("diabetes_model.pkl")

# data validation schema
# this allow the api to validate incoming data
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    BMI: float
    Age: int

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # return {"message": "Diabetes Prediction API is live"}
    return templates.TemplateResponse("index.html", {"request": request, "data": "Hello from FastAPI!"})



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

@app.post("/submit")
async def submit_form(request: Request):
    form = await request.form()
    input_data = np.array([[int(form['Pregnancies']),
                            float(form['Glucose']),
                            float(form['BloodPressure']),
                            float(form['BMI']),
                            int(form['Age'])]])
    prediction = model.predict(input_data)[0]
    if prediction == 0:
        diagnosis = "the person is not diabetic"
    elif prediction == 1:
        diagnosis = "the person is diabetic"
    else:
        diagnosis = "Error in prediction"
        
    return templates.TemplateResponse("index.html", {"request": request, "msg": diagnosis})
