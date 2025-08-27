# 💊 Medical Chatbot with Streamlit & Ollama

An interactive **AI-powered medical Q\&A chatbot** built with **Streamlit** and **Ollama** (using the Llama 3.2 model).
This app provides helpful responses to **medical and pharmacy-related questions only**.

⚠️ **Disclaimer**: This chatbot is for educational and informational purposes only. It does not replace professional medical advice. Always consult a licensed healthcare provider for real medical concerns.

---

## 🚀 Features

* 💬 **Interactive Chat UI** using Streamlit’s chat components
* 🧠 **Powered by Ollama** with the Llama 3.2 model
* ⏱ **Streaming responses** for a natural conversational flow
* 📜 **Chat history persistence** across messages in a session
* 🩺 **Medical context enforcement** via system prompts

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
cd medical-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` should include:

```
streamlit
requests
```

### 3. Install & Run Ollama

Follow instructions from [Ollama’s website](https://ollama.ai/) to install.
Then pull the **Llama 3.2** model:

```bash
ollama pull llama3.2
```

Run Ollama locally (default API runs on `http://localhost:11434`):

```bash
ollama serve
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

---

## ⚙️ Configuration

By default, the app is configured to:

* API URL: `http://localhost:11434/v1/chat/completions`
* Model: `llama3.2`

You can update these values in `app.py`:

```python
OLLAMA_API_URL = "http://localhost:11434/v1/chat/completions"
OLLAMA_MODEL = "llama3.2"
```

---

## 🖥️ Usage

1. Open your browser at `http://localhost:8501`
2. Type a **medical or pharmacy-related question** in the chat input
3. Receive a **streamed AI-powered response** in real-time

Example questions:

* “What are common side effects of ibuprofen?”
* “How do beta-blockers work?”
* “What’s the difference between a viral and bacterial infection?”

---

## 🔧 Project Structure

```
medical-chatbot/
│── app.py              # Streamlit app with Ollama integration
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
```

---

## 📜 License

MIT License – feel free to use and modify for your own projects.

---

Would you like me to also generate a **ready-to-use `requirements.txt`** file for this chatbot so you can run it immediately?
