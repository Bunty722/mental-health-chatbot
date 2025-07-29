# AI Chatbot for Mental Health Support

This project is a conversational AI agent designed to provide basic, empathetic emotional support. It features a custom-tuned language model served via a Python backend and a user-friendly web interface.

---

## ✨ Features

- **Empathetic Responses:** The core of the chatbot is a `microsoft/DialoGPT-small` model fine-tuned on the `empathetic_dialogues` dataset, enabling it to provide more supportive and understanding responses.
- **Web Interface:** A clean and simple chat interface built with Streamlit allows for easy interaction.
- **API Backend:** A lightweight Flask server hosts the fine-tuned model, making it accessible via an API.
- **Conversation Logging:** All interactions are logged to a `chat_log.log` file for monitoring and future analysis.
- **Local Deployment:** The entire application is configured to run locally on your machine.

---

## 🛠️ Technologies Used

- **AI/ML:** Python, PyTorch, Hugging Face (`transformers`, `datasets`)
- **Backend:** Flask
- **Frontend:** Streamlit
- **Environment:** Anaconda

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 1. Prerequisites

- Anaconda (or Miniconda) installed.
- Git installed.
- The fine-tuned model folder (`mental-health-chatbot-final`) must be present in the root directory.

### 2. Setup

First, clone the repository and set up the Conda environment.

```bash
# Clone this repository
git clone https://github.com/Bunty722/mental-health-chatbot
cd your-repo-name

# Create the Conda environment from the requirements file
conda create --name mental_health_chatbot_env python=3.10 -y
conda activate mental_health_chatbot_env

# Install all required packages
pip install -r requirements.txt
```

### 3. Running the Application

You need to run the backend and frontend servers in two separate terminals.

**Terminal 1: Start the Backend**
```bash
# Make sure your environment is active
conda activate mental_health_chatbot_env

# Run the Flask API server
python app.py
```
The server will start, and you will see a message confirming that the model has been loaded successfully.

**Terminal 2: Start the Frontend**
```bash
# Make sure your environment is active
conda activate mental_health_chatbot_env

# Run the Streamlit UI
streamlit run frontend.py
```

A new tab should automatically open in your web browser at `http://localhost:8501`, where you can interact with the chatbot.
