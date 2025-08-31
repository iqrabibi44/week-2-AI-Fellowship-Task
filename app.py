import streamlit as st
from personas import personas
from ai_personas import ai_response

st.title("🗨️ Persona Chatbot")
st.write("Choose a persona and start chatting!")

mode = st.radio("Choose Mode:", ["Offline Rule-Based", "AI-Powered"])
is_ai = mode == "AI-Powered"

persona_choice = st.selectbox("Choose a Persona:", list(personas.keys()))
persona_fn = personas[persona_choice]

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You: ", "")

if st.button("Send") and user_input:
    if is_ai:
        response = ai_response(user_input, persona_choice)
    else:
        response = persona_fn(user_input)

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append((persona_choice, response))

for speaker, text in st.session_state.history:
    st.markdown(f"**{speaker}:** {text}")
