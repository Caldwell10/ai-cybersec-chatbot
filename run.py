from flask import Flask
from app.routes import chatbot

# Initialize Flask
app = Flask(__name__)

# Register the chatbot routes
app.register_blueprint(chatbot)

if __name__ == '__main__':
    app.run(debug=True)