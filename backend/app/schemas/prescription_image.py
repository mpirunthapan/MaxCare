from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PrescriptionImageOut(BaseModel):
    id: UUID
    prescription_id: UUID
    image_url: str
    created_at: datetime

    class Config:
        orm_mode = True