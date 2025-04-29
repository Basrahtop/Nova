from fastapi import FastAPI, HTTPException
from ai_engine import generate_lesson

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "NOVA AI Tutor API Running"}

@app.post("/generate-lesson/")
async def get_lesson(student_input: dict):
    try:
        subject = student_input.get("subject", "math")
        result = generate_lesson(subject)
        return {"lesson": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
