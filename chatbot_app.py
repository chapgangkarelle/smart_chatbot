import streamlit as st
import os
from mistralai import Mistral


# Configuration de l'API Mistral
api_key = "9F8Lnhk8zfkxKxj3EfCyY3j9RzIaVwjB"
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

# Fonction pour générer une réponse via l'API Mistral
def generate_response(user_input):
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": user_input,
            },
        ]
    )
    return chat_response.choices[0].message.content

# Interface Streamlit
st.title("Chatbot avec Streamlit")
st.write("Bienvenue sur l'interface de chatbot. Posez-moi des questions !")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Formulaire pour entrer du texte
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Vous :", key="input")
    submit_button = st.form_submit_button(label='Envoyer')

if submit_button and user_input:
    response = generate_response(user_input)  # Appel à la fonction generate_response
    # Ajouter l'entrée utilisateur et la réponse à l'historique
    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Affichage des messages
for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")

