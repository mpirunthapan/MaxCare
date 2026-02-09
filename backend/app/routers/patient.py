from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/")
def create_patient():
    return {"message": "Create patient"}

@router.get("/")
def list_patients(db: Session = Depends(get_db)):
    return {"message": "List patients"}

@router.get("/{patient_id}")
def get_patient(patient_id: str, db: Session = Depends(get_db)):
    return {"message": f"Get patient with ID {patient_id}"}