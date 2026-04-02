def grade(final_state):
    score = 0.0

    if final_state.get("final_answer"):
        score += 0.4

    if len(final_state.get("collected_info", [])) >= 2:
        score += 0.2

    if len(final_state.get("options", [])) >= 1:
        score += 0.2

    if final_state.get("step", 0) <= 5:
        score += 0.2

    return min(score, 1.0)