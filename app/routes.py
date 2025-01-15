from flask import Blueprint, request, jsonify
from app.chatbot_model import get_cve_info

chatbot= Blueprint('chatbot', __name__)

@chatbot.route("/api/chat", methods=["Post"])
def chat():
    user_input = request.json.get("message", "")
    response = get_cve_info(user_input)
    return jsonify({"response": response})

