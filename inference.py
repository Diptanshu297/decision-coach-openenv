from env.environment import DecisionCoachEnv
from utils.prompt_builder import build_prompt
from utils.action_parser import parse_action

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
import os
from env.grader import grade

# 🔑 LLM client
client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("API_KEY")
)


# 🤖 LLM call
def call_llm(prompt):
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[
            {
                "role": "system",
                "content": "You are a decision-making agent. Respond ONLY in JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


# 🚀 INIT ENV
env = DecisionCoachEnv()
state = env.reset()

done = False
max_steps = 5


# 🔁 MAIN LOOP
while not done and state["step"] < max_steps:

    prompt = build_prompt(state)

    # 🔥 FORCE FINAL STEP (VERY IMPORTANT)
    if state["step"] == max_steps - 1:
        action = {
            "type": "final_recommendation",
            "content": "Based on available information, this is the best decision."
        }
        print("[FORCED FINAL STEP]")
    else:
        response = call_llm(prompt)
        print("RAW RESPONSE:", response)  # debug

        action = parse_action(response)

    # ⚙️ step environment
    state, reward, done, _ = env.step(action)

    # 📊 logging
    print(f"[STEP {state['step']}] {action['type']} | reward={reward}")

final_score = grade(state)
print(f"[FINAL SCORE]: {final_score}")
print("[END]")