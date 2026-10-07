import json
from typing import Dict, Any
from pydantic import BaseModel, Field
from groq import Groq
from config.settings import GROQ_API_KEY

class TaskParsed(BaseModel):
    title: str = Field(description="Título legível e resumido da tarefa")
    duration_minutes: int = Field(description="Tempo estimado em minutos. Padrão: 30")
    energy: str = Field(description="Nível de energia necessário: 'baixa', 'media' ou 'alta'")
    priority: int = Field(description="Prioridade de 1 (baixa) a 3 (alta)")
    category: str = Field(description="Categoria curta (ex: domestico, trabalho, estudos, pessoal)")

class TaskParserService:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = "openai/gpt-oss-120b" 

    def parse_text_to_task(self, user_message: str) -> Dict[str, Any]:
        """
        Recebe o texto livre do Telegram e converte em um dicionário padronizado.
        """
        system_prompt = (
            "Você é um assistente extrator de tarefas. Sua única função é analisar a mensagem do usuário "
            "e extrair os dados da tarefa em formato JSON estrito.\n"
            "Regras:\n"
            "- 'title': título resumido da tarefa (string).\n"
            "- 'duration_minutes': estimativa em minutos (inteiro). Se não informado, use 30.\n"
            "- 'energy': uma estimativa do nível de energia necessário para executar a tarefa. Se não for fornecida, estime. Deve ser estritamente 'baixa', 'media' ou 'alta'. Se não souber, use 'media'.\n"
            "- 'priority': inteiro de 1 a 3 (1=baixa, 2=média, 3=alta).\n"
            "- 'category': uma palavra descrevendo o contexto. As possíveis categorias são: 'casa', 'mestrado', 'pessoal'. Nunca escolha uma categoria que não esteja na lista.\n"
            "- Responda APENAS com o objeto JSON sem marcadores markdown ou explicações adicionais."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Extraia a tarefa da seguinte mensagem: '{user_message}'"}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Mensagem: '{user_message}'"}
                ],
                temperature=0.1,
                response_format={"type": "json_object"}
            )
            
            raw_text = response.choices[0].message.content.strip()
            parsed_json = json.loads(raw_text)
            
            # Validação Pydantic
            task_data = TaskParsed(**parsed_json)
            return task_data.model_dump()

        except Exception as e:
            print(f"Erro no parsing da tarefa: {e}")
            # Fallback caso o modelo falhe em formatar
            return {
                "title": user_message,
                "duration_minutes": 30,
                "energy": "media",
                "priority": 2,
                "category": "geral"
            }