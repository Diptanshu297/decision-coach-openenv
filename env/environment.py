class DecisionCoachEnv:

    def __init__(self):
        self.state = None

    def reset(self):
        self.state = {
            "user_problem": "I am confused about my career",
            "conversation_history": [],
            "step": 0,
            "collected_info": [],
            "options": [],
            "final_answer": None
        }
        return self.state

    def step(self, action):

        self.state["step"] += 1

        
        self.state["conversation_history"].append(action)

        
        if action["type"] == "ask_clarifying_question":
            self.state["collected_info"].append(action["content"])

        elif action["type"] == "generate_options":
            self.state["options"].append(action["content"])

        elif action["type"] == "final_recommendation":
            self.state["final_answer"] = action["content"]

        
        from env.reward import compute_reward
        reward = compute_reward(action, self.state)

        
        done = False
        if action["type"] == "final_recommendation" or self.state["step"] >= 5:
            done = True

        return self.state, reward, done, {}