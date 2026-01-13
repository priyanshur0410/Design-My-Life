from pydantic import BaseModel
from datetime import datetime

class Activity(BaseModel):
    goal_id: str
    activity_type: str  # Learning, Health
    value: int          # minutes or reps
    timestamp: datetime
