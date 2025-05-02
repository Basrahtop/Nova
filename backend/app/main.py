from fastapi import FastAPI
from app.routes import auth, tutor
from app.database import create_tables

app = FastAPI(title="Nova Backend", description="AI Tutor for Africans", version="1.0")

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(tutor.router, prefix="/tutor", tags=["AI Tutor"])

# Initialize database tables
@app.on_event("startup")
async def startup_event():
    create_tables()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Nova Backend API!"}