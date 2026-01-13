from datetime import datetime, timedelta
from collections import defaultdict
from app.repositories.base import ActivityRepository

class InsightService:

    def __init__(self, repo: ActivityRepository):
        self.repo = repo

    def consistency_score(self, goal_id: str) -> float:
        activities = self.repo.get_by_goal(goal_id)
        if not activities:
            return 0.0

        dates = sorted({a.timestamp.date() for a in activities})
        streak = 1
        max_streak = 1

        for i in range(1, len(dates)):
            if (dates[i] - dates[i - 1]).days == 1:
                streak += 1
                max_streak = max(max_streak, streak)
            else:
                streak = 1

        return round(max_streak / len(dates), 2)

    def health_threshold_alert(self, goal_id: str) -> bool:
        one_week_ago = datetime.utcnow() - timedelta(days=7)
        activities = self.repo.get_by_goal(goal_id)

        total_health_minutes = sum(
            a.value for a in activities
            if a.activity_type.lower() == "health" and a.timestamp >= one_week_ago
        )

        return total_health_minutes < 150

    def recommendation_engine(self) -> str:
        activities = self.repo.get_all()
        learning = sum(a.value for a in activities if a.activity_type.lower() == "learning")
        health = sum(a.value for a in activities if a.activity_type.lower() == "health")

        if learning > 300 and health < 150:
            return "You are excelling in learning but neglecting physical wellness. Consider rebalancing your growth plan."
        return "Your growth plan appears balanced. Keep going!"
