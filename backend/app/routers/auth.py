from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login():
    return {"message": "Login route"}

@router.post("/register")
def register():
    return {"message": "Register route"}