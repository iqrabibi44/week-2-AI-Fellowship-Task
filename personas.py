def professional_assistant(user_input):
    return f"As your professional assistant, I suggest: '{user_input}' sounds like something we can solve step by step."

def creative_companion(user_input):
    return f"✨ Imagine this: '{user_input}' as a story unfolding into something magical!"

def casual_friend(user_input):
    return f"Yo! That '{user_input}' sounds cool 😎. Let’s chill and talk more about it."

personas = {
    "Professional Assistant": professional_assistant,
    "Creative Companion": creative_companion,
    "Casual Friend": casual_friend,
}
