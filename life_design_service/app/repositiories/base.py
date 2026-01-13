from abc import ABC, abstractmethod
from typing import List
from app.models.activity import Activity

class ActivityRepository(ABC):

    @abstractmethod
    def add_activity(self, activity: Activity):
        pass

    @abstractmethod
    def get_by_goal(self, goal_id: str) -> List[Activity]:
        pass

    @abstractmethod
    def get_all(self) -> List[Activity]:
        pass
