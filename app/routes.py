from flask import Blueprint, request, jsonify
from app.chatbot_model import get_cve_info, search_cve_by_keyword, filter_cve_by_severity

chatbot= Blueprint('chatbot', __name__)

# Route for chatbot conversation
@chatbot.route("/api/chat", methods=["Post"])
def chat():
    user_input = request.json.get("message", "")
    response = get_cve_info(user_input)
    return jsonify({"response": response})

# Route for searching CVEs by keyword
@chatbot.route("/api/search", methods=["POST"])
def search():
    keyword =request.json.get("keyword", "").strip()
    response= search_cve_by_keyword(keyword)
    return jsonify({"response": response})

#Route for filtering CVEs by severity
@chatbot.route("/api/filter", methods=["POST"])
def filter():
    severity =request.json.get("severity", "").strip()
    response= filter_cve_by_severity(severity)
    return jsonify({"response": response})

