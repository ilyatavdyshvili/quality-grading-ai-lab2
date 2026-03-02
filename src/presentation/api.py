from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

from src.infrastructure.storage import S3Storage
from src.application.services import DataSyncService, SalaryPredictionService

load_dotenv()

app = FastAPI()


class SalaryRequest(BaseModel):
    experience: int


# Dependency Injection
storage = S3Storage(
    endpoint_url=os.getenv("MINIO_ENDPOINT"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    bucket=os.getenv("MINIO_BUCKET")
)

sync_service = DataSyncService(storage)
salary_service = SalaryPredictionService(sync_service)


@app.post("/predict")
def predict_salary(request: SalaryRequest):
    prediction = salary_service.predict_salary(request.experience)
    return {"predicted_salary": prediction}