from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import InteractionCreate, InteractionResponse
from app.crud import create_interaction
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/query", response_model=InteractionResponse)
async def ask_tutor(interaction: InteractionCreate, db: Session = Depends(get_db)):
    # Simulate AI response (replace with actual AI integration)
    ai_response = f"Simulated AI response for query: {interaction.query}"
    interaction.response = ai_response
    return create_interaction(db, interaction)