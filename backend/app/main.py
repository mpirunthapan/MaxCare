from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, patient, prescription

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MaxCare API",
    description="API for MaxCare healthcare management system",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(patient.router)
app.include_router(prescription.router)

@app.get("/")
def root():
    return {"message": "Welcome to MaxCare API"}