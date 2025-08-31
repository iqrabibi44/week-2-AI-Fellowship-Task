from personas import personas
from ai_personas import ai_response

def chat_loop():
    print("Chatbot CLI is running... (type 'quit' to exit)\n")

    mode = input("Choose mode: (1) Offline Rule-Based  (2) AI-Powered: ")
    is_ai = mode.strip() == "2"

    print("\nAvailable Personas:")
    persona_names = list(personas.keys())
    for i, persona in enumerate(persona_names, 1):
        print(f"{i}. {persona}")
    choice = int(input("\nSelect persona (1-3): "))
    persona_name = persona_names[choice - 1]
    persona_fn = personas[persona_name]

    conversation_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break

        if is_ai:
            response = ai_response(user_input, persona_name)
        else:
            response = persona_fn(user_input)

        conversation_history.append(("You", user_input))
        conversation_history.append((persona_name, response))

        print(f"{persona_name}: {response}")

if __name__ == "__main__":
    chat_loop()
