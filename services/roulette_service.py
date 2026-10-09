from typing import Optional
from database.repositories.task_repository import TaskRepository
import random

class RouletteService:
    def __init__(self, task_repo: Optional[TaskRepository] = None):
        self.task_repo = task_repo or TaskRepository()


    def spin(self, max_duration: int, energy_level: str) -> str:
        """Retorna uma tarefa aleatória da lista de tarefas elegíveis."""

        tasks = self.task_repo.get_eligible_tasks(max_duration, energy_level)
        print(f"Tarefas elegíveis encontradas: {tasks}")
        if not tasks:
            return "Nenhuma tarefa elegível encontrada."
        
        weights = [task["priority"] for task in tasks]

        eligible_tasks = []
        time_taken = 0
        while time_taken < max_duration:
            task = random.choices(tasks, weights=weights)[0]
            if time_taken + task["duration_minutes"] <= max_duration:
                eligible_tasks.append(task)
                time_taken += task["duration_minutes"]
            else:
                break
        return eligible_tasks if eligible_tasks else "Nenhuma tarefa elegível encontrada dentro do tempo disponível."