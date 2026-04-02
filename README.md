📄 🧠 README.md (Developer Guide)
# Decision Coach OpenEnv

## 🧠 What This Project Is

This is an **OpenEnv-based RL environment** where an AI agent acts as a **decision-making counsellor**.

The agent:
- understands a user problem
- asks questions
- generates options
- evaluates them
- gives a final recommendation

---

## ⚙️ Project Structure
project-root/
│
├── inference.py # Runs the agent loop (ENTRY POINT)
├── openenv.yaml # OpenEnv config
├── Dockerfile # Deployment
├── requirements.txt
│
├── env/ # Core environment logic
│ ├── environment.py # reset() and step()
│ ├── state.py # state structure
│ ├── actions.py # action types
│ ├── reward.py # reward logic
│ ├── grader.py # final scoring
│ └── tasks/ # easy / medium / hard cases
│
└── utils/
├── prompt_builder.py
├── action_parser.py


---

## 🔄 How The System Works

### Step-by-step flow:

1. `env.reset()`
   - loads a task
   - initializes state

2. Loop starts:
state → LLM → action → env.step(action)


3. Inside `step()`:
- update conversation history
- compute reward
- check if done

4. Loop continues until:
- final decision OR max steps

5. `grader()` runs → gives final score (0–1)

---

## 🤖 Inference Flow (inference.py)
env.reset()

while not done:
→ build prompt from state
→ call LLM (HF/OpenAI)
→ parse action
→ env.step(action)

after done:
→ grader()


---

## 🔑 API + Tokens

### Hugging Face (FINAL)
Used in production:
HF_TOKEN=<your_token>
API_BASE_URL=<hf_endpoint>


Used inside:
inference.py (OpenAI client)


---

### OpenAI (ONLY for testing, optional)
OPENAI_API_KEY=xxx
API_BASE_URL=https://api.openai.com/v1


👉 Faster for local debugging

---

## ▶️ How to Run Locally

### 1. Setup venv
uv venv
.venv\Scripts\activate


### 2. Install deps
uv pip install -r requirements.txt


### 3. Run project
python inference.py


---

## 🧩 Action Format (IMPORTANT)

LLM MUST return:

```json
{
  "type": "ask_clarifying_question",
  "content": "What are your interests?"
}
🎯 Action Types
analyze_user_profile

ask_clarifying_question

generate_options

evaluate_tradeoffs

final_recommendation

🧪 Tasks
Located in:

env/tasks/
Types:

easy

medium

hard

🏆 Reward vs Grader
Reward → given every step (inside step())

Grader → final score after completion

🐳 Docker
docker build -t decision-env .
docker run decision-env
⚠️ Important Rules
inference.py MUST be in root

Dockerfile MUST be in root

Do NOT include .venv

Keep imports clean

👥 Team Responsibilities
Environment → env/

Inference → inference.py

Deployment → Docker + HF

Reward/Grader → shared

🧠 Quick Mental Model
STATE → LLM → ACTION → ENV → REWARD → LOOP → GRADER
❓ If Something Breaks
Check:

imports

env.step() return format

API keys

JSON parsing of actions


---

# ⚡ Why this is good

- No fluff ✅  
- Dev-focused ✅  
- Explains flow clearly ✅  
- Helps teammates jump in fast ✅  

---

If you want next, I can:
👉 trim this into a **1-page cheat sheet your team can pin while coding**
