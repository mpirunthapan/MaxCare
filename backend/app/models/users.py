from sqlalchemy import column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.models.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = column(String, unique=True, index=True, nullable=False)
    password_hash = column(String, nullable=False)
    full_name = column(String, nullable=True)
    role = column(String, default="doctor")
    created_at = column(datetime, default=datetime.utcnow)