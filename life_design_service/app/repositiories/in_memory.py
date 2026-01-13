from typing import List
from app.models.activity import Activity
from app.repositories.base import ActivityRepository

class InMemoryActivityRepository(ActivityRepository):

    def __init__(self):
        self._activities: List[Activity] = []

    def add_activity(self, activity: Activity):
        self._activities.append(activity)

    def get_by_goal(self, goal_id: str) -> List[Activity]:
        return [a for a in self._activities if a.goal_id == goal_id]

    def get_all(self) -> List[Activity]:
        return self._activities
