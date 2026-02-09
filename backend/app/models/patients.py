from sqlalchemy import column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.models.base import Base
from datetime import datetime

class Patient(Base):
    __tablename__ = "patients"

    id = column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = column(String, nullable=False)
    age = column(Integer, nullable=False)
    gender = column(String, nullable=False)
    phone = column(String, index=True)
    address = column(String)
    created_at = column(DateTime, default=datetime.utcnow)