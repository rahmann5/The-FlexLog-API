import httpx
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

# Initialize the FastAPI app instance
app = FastAPI(title="The FlexLog API")

class Exercise(BaseModel):
    name: str
    sets: int
    reps: int
    weight: float
    comment: Optional[str] = None
    
workout_db: List[Exercise] = []

@app.get("/")
async def health_check():
    return {
        "service": "FlexLog API",
        "status": "Online",
        "version": "1.0.0"
    }

@app.post("/log-exercise")
async def log_exercise(exercise: Exercise):
    workout_db.append(exercise)
    return {"message": f"Successfully logged {exercise.name}!", "data": exercise}

@app.post("/log-excercises")
async def log_excercises(items: list[Exercise]):
    workout_db.extend(items)
    return {"message": f"Successfully logged all exercises"}

@app.get("/history")
async def get_history():
    return workout_db

@app.get("/stats")
async def total_volume():
    volume = 0
    for exercise in workout_db:
        volume += (exercise.sets * exercise.reps * exercise.weight)
    tip = await get_motivation()
    return {"total_volume": volume, "unit": "kg", "tip": tip}

@app.get("/pr/{exercise_name}")
async def get_personal_record(exercise_name : str):
    matched_workouts = []
    for workout in workout_db:
        if workout.name.lower() == exercise_name.lower():
            matched_workouts.append(workout)
    
    if len(matched_workouts) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"No records found for the exercise {exercise_name}"
        )
    
    personal_record_exercise = max(matched_workouts, key=lambda exercise: exercise.weight)

    return {"exercise":personal_record_exercise.name, "personal record weight":personal_record_exercise.weight, "full details": personal_record_exercise}


async def get_motivation():
    """
    Fetches a random tip from an external API without blocking the server.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get("https://api.adviceslip.com/advice", timeout=5.0)
            data = response.json()
            # The Advice Slip API returns: {"slip": {"id": 321, "advice": "Advice text"}}
            return data["slip"]["advice"]
        except Exception:
            # Error retrieving advice slip return a generic motivational comment
            return "Keep pushing! Consistency is key."
