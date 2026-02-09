from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List

class PrescriptionCreate(BaseModel):
    patient_id: UUID
    doctor_name: str

class PrescriptionUpdate(BaseModel):
    notes: Optional[str] = None

class PrescriptionOut(BaseModel):
    id: UUID
    patient_id: UUID
    visit_date: datetime
    notes: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True