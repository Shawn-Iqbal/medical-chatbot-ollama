import streamlit as st
import requests
import json

OLLAMA_API_URL = "http://localhost:11434/v1/chat/completions"
OLLAMA_MODEL = "llama3.2" 

st.set_page_config(page_title="Medical Chatbot", page_icon="💊")
st.title("💬 Ask Me Anything - Medical Edition")
st.caption("For medical and pharmacy-related questions only.")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! Ask me any medical or health-related question. 💊"}]

# Render chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user prompt
if prompt := st.chat_input("Ask your medical question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        try:
            payload = {
                "model": OLLAMA_MODEL,
                "stream": True,
                "messages": [
                    {"role": "system", "content": "You are a helpful medical assistant. Only answer medical and health-related questions."},
                    {"role": "user", "content": prompt}
                ]
            }

            response = requests.post(OLLAMA_API_URL, json=payload, stream=True)

            for line in response.iter_lines():
                if line:
                    line = line.decode("utf-8").strip()
                    if line.startswith("data: "):
                        line = line.removeprefix("data: ").strip()
                    if line == "[DONE]":
                        break
                    try:
                        chunk = json.loads(line)
                        delta = chunk.get("choices", [{}])[0].get("delta", {})
                        content = delta.get("content", "")
                        full_response += content
                        placeholder.markdown(full_response + "▌")
                    except json.JSONDecodeError:
                        continue

            placeholder.markdown(full_response)

        except Exception as e:
            full_response = f"⚠️ Error talking to Ollama: {e}"
            placeholder.markdown(full_response)
        

    st.session_state.messages.append({"role": "assistant", "content": full_response})
