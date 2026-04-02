class DecisionCoachEnv:

    def __init__(self):
        self.state = None

    def reset(self):
        self.state = {
            "user_problem": "I am confused about my career",
            "conversation_history": [],
            "step": 0
        }
        return self.state

    def step(self, action):
        self.state["conversation_history"].append(action)
        self.state["step"] += 1

        reward = 0.0
        done = False

        if action["type"] == "final_recommendation":
            done = True

        return self.state, reward, done, {}