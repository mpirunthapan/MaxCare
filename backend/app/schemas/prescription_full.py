from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List

from app.schemas.prescription_image import PrescriptionImageOut

class PrescriptionFullOut(BaseModel):
    id: UUID
    patient_id: UUID
    visit_date: datetime
    notes: Optional[str]
    created_at: datetime
    images: List[PrescriptionImageOut]

    class Config:
        orm_mode = True