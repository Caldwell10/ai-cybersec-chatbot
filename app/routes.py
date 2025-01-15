from flask import Blueprint, request, jsonify
from app.chatbot_model import get_cve_info

chatbot= Blueprint('chatbot', __name__)