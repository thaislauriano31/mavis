from typing import List, Dict, Any, Optional
from database.client import supabase

class TaskRepository:
    def __init__(self):
        self.client = supabase

    def create_task(
        self, 
        title: str, 
        duration_minutes: int, 
        energy: str, 
        priority: int = 2, 
        category: str = "geral"
    ) -> Dict[str, Any]:
        """Cadastra uma nova tarefa pendente no banco de dados."""
        data = {
            "title": title,
            "duration_minutes": duration_minutes,
            "energy": energy,
            "priority": priority,
            "category": category,
            "status": "pendente"
        }
        response = self.client.table("tasks").insert(data).execute()
        return response.data[0] if response.data else {}

    def get_eligible_tasks(self, max_duration: int, energy_level: str) -> List[Dict[str, Any]]:
        """
        Busca tarefas pendentes que:
        - Caibam no tempo disponível (duration_minutes <= max_duration)
        - Correspondam ao nível de energia informado
        - Não sejam tarefas inegociáveis registradas para o dia
        """
        response = (
            self.client.table("tasks")
            .select("*")
            .eq("status", "pendente")
            .eq("is_non_negotiable", False)
            .lte("duration_minutes", max_duration)
            .eq("energy", energy_level)
            .order("priority", desc=True)
            .execute()
        )
        return response.data

    def mark_as_completed(self, task_id: str) -> Optional[Dict[str, Any]]:
        """Marca uma tarefa como concluída."""
        response = (
            self.client.table("tasks")
            .update({"status": "concluida"})
            .eq("id", task_id)
            .execute()
        )
        return response.data[0] if response.data else None