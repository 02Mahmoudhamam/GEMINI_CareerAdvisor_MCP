# GEMINI_CAREER_MCP

**GEMINI_CAREER_MCP** is a Multi-Agent AI System built using FastAPI and Google's Gemini API.  
It enables intelligent routing and processing of user queries (text or images) to provide smart career advice, powered by LLM agents working in orchestration.

---

## 🧠 System Overview

The system uses a **Multi-Component Pipeline (MCP)** architecture with the following agents:

- **Orchestrator**: Receives requests and coordinates the process.
- **Router Agent**: Classifies the input type (text/image).
- **Text Agent**: Handles and analyzes textual content.
- **Image Agent**: Processes visual input.
- **Career Advisor Agent**: Generates career guidance and recommendations based on the analysis.

---

## ⚙️ Architecture

📥 user_input
      |
      ▼
🧠 MCP_Orchestrator
      |
 ┌────────────┬──────────────┐
 ▼            ▼              ▼
🔍 Router   📝 Text Agent   🖼️ Image Agent
                |
                ▼
     📊 Career Advisor Agent
                ▼
       🧾 Output: Report & Recommendation
 

## 2. Install dependencies

pip install -r requirements.txt
Make sure your .env file contains your Gemini API Key as:
GEMINI_API_KEY=your_key_here

## 3. Run all servers in separate terminals

# Terminal 1 - Orchestrator
uvicorn orchestrator.main:app --reload --port 8000

# Terminal 2 - Router
uvicorn router.main:app --reload --port 8001

# Terminal 3 - Text Agent
uvicorn text_agent.main:app --reload --port 8002

# Terminal 4 - Image Agent
uvicorn image_agent.main:app --reload --port 8003

# Terminal 5 - Career Advisor Agent
uvicorn career_advisor_agent.main:app --reload --port 8004
📂 Project Structure

GEMINI_CAREER_MCP/
├── orchestrator/
│   └── main.py
├── router/
│   └── main.py
├── text_agent/
│   └── main.py
├── image_agent/
│   └── main.py
├── career_advisor_agent/
│   └── main.py
├── shared/
│   └── utils.py
├── requirements.txt
├── .env
└── README.md
🧪 Sample Request (via Swagger UI)
Go to:
http://127.0.0.1:8000/docs

Use the /process endpoint

Upload either:

📄 A text file (plain text)

🖼️ An image file (PNG/JPG)

Fill the interests field with relevant career interests (e.g. AI, Robotics, Data Science)

Example:


interests: AI, Robotics, Space
file: resume.png
✅ The system will analyze your input and return career guidance.

## 📌 Notes
For image inputs, response time may vary based on image complexity.

Timeout settings can be adjusted in the Orchestrator and Router as needed.

All agents are decoupled and can be extended or replaced individually.

## 📃 License
This project is for educational and demonstration purposes.
No commercial license is granted.


---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/02Mahmoudhamam/GEMINI_CAREER_MCP.git
cd GEMINI_CAREER_MCP

