# Local CrewAI Research Agent

A simple multi-agent automation script built using **CrewAI** and Python to research topics, analyze market trends, and generate structured content.

---

## 🛠️ Prerequisites

* Python 3.10 or higher
* An active virtual environment (`dev-env`)

---

## 📦 Installation & Setup

1.Clone or navigate to the project directory:

Activate your virtual environment:

PowerShell
# If using Windows PowerShell
..\dev-env\Scripts\Activate.ps1
Install the required dependencies:

PowerShell
pip install crewai pydantic
(Note: Make sure you also install any LLM provider packages you are using, such as crewai[tools] or OpenAI/Ollama packages).

🚀 Usage
Run the local agent script using Python:

PowerShell
python local_agent.py
🧩 Project Structure
local_agent.py — Main entry point containing agent definitions, tasks, and the Crew setup.

README.md — Project documentation and setup guide.

⚠️ Troubleshooting
If you encounter a ValidationError: Agent is missing in the task, ensure that:

Every Task object explicitly defines its assigned agent using the singular parameter: agent=your_agent_name.

All task variables are properly registered inside the Crew(tasks=[...]) list.

You have saved (Ctrl + S) your script before running it again in the terminal.
