from env.environment import DecisionCoachEnv

env = DecisionCoachEnv()
state = env.reset()

done = False
max_steps = 5  # 🔥 prevents infinite loop

while not done and state["step"] < max_steps:

    # 🔁 simulate progression (VERY IMPORTANT)
    if state["step"] < 2:
        action = {
            "type": "ask_clarifying_question",
            "content": "What are your interests?"
        }
    elif state["step"] < 4:
        action = {
            "type": "generate_options",
            "content": "Here are some career options..."
        }
    else:
        action = {
            "type": "final_recommendation",
            "content": "Based on your interests, you should choose X"
        }

    state, reward, done, _ = env.step(action)

    print(f"[STEP {state['step']}] {action['type']} | reward={reward}")

print("[END]")