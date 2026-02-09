from typing import List
from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/prescriptions", tags=["Prescriptions"])

@router.post("/upload")
async def upload_prescription(files: List[UploadFile] = File(...)):
    return [
        {
        "filename": file.filename,
        "content_type": file.content_type,
        }
        for file in files
    ]
