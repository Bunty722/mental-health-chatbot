# app.py (Final Version with Logging)
import torch
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import logging # Import the logging library

# --- 1. SETUP LOGGING ---
# This will save logs to a file named 'chat_log.log'
logging.basicConfig(filename='chat_log.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# --- 2. SETUP MODEL ---
app = Flask(__name__)
print("Loading fine-tuned model...")
model_name = "./mental-health-chatbot-final"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
print("Model loaded successfully!")

# --- 3. API ENDPOINT ---
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    chat_history_ids_tensor = request.json.get('history')
    
    # Let the AI model handle the response
    if chat_history_ids_tensor:
        chat_history_ids = torch.tensor(chat_history_ids_tensor)
    else:
        chat_history_ids = None

    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids is not None else new_user_input_ids
    attention_mask = torch.ones_like(bot_input_ids)
    
    chat_history_ids = model.generate(
        bot_input_ids, attention_mask=attention_mask, max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id, do_sample=True, top_k=50, temperature=0.75
    )
    
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    # --- NEW: Log the conversation ---
    logging.info(f"User: {user_input} | Bot: {response}")
    # --- END OF LOGIC ---
    
    return jsonify({ 'response': response, 'history': chat_history_ids.tolist() })

@app.route('/', methods=['GET'])
def health_check():
    return "API is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)