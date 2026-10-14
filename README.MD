# 🎰 Mavis — Assistente Pessoal & Roleta de Tarefas

**Mavis** é uma assistente pessoal no Telegram projetada para reduzir a paralisia de decisão e organizar a rotina diária através de uma **roleta inteligente de tarefas**, respeitando o tempo disponível e o nível de energia do momento.

---

## 🎯 Problema que Resolve

Muitas vezes ficamos paralisados tentando decidir qual tarefa realizar nos momentos livres ou de foco. A Mavis automatiza essa escolha sorteando tarefas pendentes que se encaixam exatamente na quantidade de tempo e energia que você tem no momento, além de manter o foco diário com tarefas inegociáveis.

---

## 🚀 Funcionalidades

### ⚙️ Fase 1 (MVP - Funcionalidades Principais)
- [X] **Captura de Tarefas via Telegram:** Envio simples de tarefas informando nome, tempo estimado, nível de energia e prioridade.
- [X] **Roleta Inteligente de Tarefas:** Sorteio automático de tarefas com base nos filtros de tempo disponível e nível de energia atual.
- [X] **Gerenciamento de Status:** Registro e baixa de tarefas executadas.

### ⏰ Fase 2 (Rotina & Acompanhamento)
- [ ] **Check-in Noturno (20h):** Pergunta automática solicitando as 1 a 3 tarefas **inegociáveis** do dia seguinte.
- [ ] **Lembrete Matinal:** Envio das prioridades inegociáveis registradas para o dia.

### 🔮 Fase 3 (Futuro)
- [ ] **Visualização Web (Streamlit):** Interface gráfica simples e gratuita para acompanhar o backlog de tarefas.
- [ ] **Integração com Google Agenda:** Sincronização e visualização dos compromissos e blocos de tempo.
- [ ] **Quebra Automática de Tarefas:** Sugestão de divisão para tarefas grandes.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Bot:** API do Telegram (`python-telegram-bot`)
- **Armazenamento:** Supabase
- **Agendamento:** `APScheduler`
