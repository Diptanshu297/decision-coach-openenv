import json
import re


VALID_TYPES = [
    "ask_clarifying_question",
    "generate_options",
    "evaluate_tradeoffs",
    "final_recommendation"
]

def parse_action(response_text):
    import json, re

    try:
        match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if match:
            action = json.loads(match.group())

            # 🔥 FIX: enforce valid type
            if action.get("type") not in VALID_TYPES:
                action["type"] = "ask_clarifying_question"

            return action
    except:
        pass

    return {
        "type": "ask_clarifying_question",
        "content": "Can you clarify more?"
    }
