from fastapi import APIRouter, Depends
from typing import List
from app.models.activity import Activity
from app.repositories.in_memory import InMemoryActivityRepository
from app.services.insights import InsightService

router = APIRouter()
repo = InMemoryActivityRepository()
service = InsightService(repo)

@router.post("/activities")
def add_activity(activity: Activity):
    repo.add_activity(activity)
    return {"message": "Activity logged successfully"}

@router.get("/dashboard/{goal_id}")
def get_dashboard(goal_id: str):
    activities = repo.get_by_goal(goal_id)
    return {
        "goal_id": goal_id,
        "total_activities": len(activities),
        "activities": activities,
        "consistency_score": service.consistency_score(goal_id),
        "wellness_warning": service.health_threshold_alert(goal_id)
    }

@router.get("/insights/optimization")
def get_optimization_insights():
    return {
        "recommendation": service.recommendation_engine()
    }
