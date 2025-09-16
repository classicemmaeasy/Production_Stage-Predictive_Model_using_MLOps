# 🩺 Diabetes Prediction Model – (FastAPI + Docker + K8s + Github Actions + AlgoCD)



End to End Machine Learning project using a real-world chronic disease use case: predicting whether a person is diabetic based on health metrics. 

 diabetes is a chronic disease, not an illness or temporary condition, characterized by persistently high blood glucose (sugar) levels. It occurs when the body produces insufficient insulin or is unable to effectively use the insulin it produces. Over time, this elevated blood sugar can lead to serious damage to many organs, including the eyes, kidneys, heart, and nerves.

 I built an End to End Supervised Machine Learning pipelines that allow users or Medical Professionals  to input different features that could potentially cause diabetes and see the result real-time.

The pipeline workflow are :

- ✅ Model Training
- ✅ Building the Model 
- ✅ API Deployment with FastAPI and a webpage for users to interact with the model. ( FastAPI enables multiple users concurently).
- ✅ Dockerization (packaging it into docker which takes my ML model with FastAPI + dependencies → packages them into a container image.)

- ✅ Kubernetes Deployment

   Kubernetes solves orchestration + scaling
   Run multiple replicas of the model API.
   Autoscale based on requests per second.
   Ensure uptime (self-healing).
   Roll out new versions of the model without downtime.

- ✅ CICD using github action
 it triggers an action anytime the code or the data changes, and automate the entire workflow in production

- ✅ Gitops using ArgoCD for deployment sync with github
---

## 📊 Problem Statement

Predict if a person is diabetic based on:
- Pregnancies
- Glucose
- Blood Pressure
- BMI
- Age

I use a Random Forest Classifier trained on the **Pima Diabetes Dataset**.

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/iam-veeramalla/first-mlops-project.git
cd first-mlops-project
```

### 2. Create Virtual Environment

```
python3 -m venv .mlops
source .mlops/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

## Train the Model

```
python train.py
```

## Run the API Locally

```
uvicorn main:app --reload
```

### Sample Input for /predict json format

```
{
  "Pregnancies": 2,
  "Glucose": 130,
  "BloodPressure": 70,
  "BMI": 28.5,
  "Age": 45
}
```

## Dockerize the API

### Build the Docker Image

```
docker build -t diabetes-model-api .
```
 
### Run the Container

```
docker run  -p 8001:8000 diabetes-model-api 
# or any port 

## Deploy to Kubernetes

kubectl apply -f diabetes-prediction-model-deployment.yaml
```





