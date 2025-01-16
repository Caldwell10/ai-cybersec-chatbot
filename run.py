from flask import Flask, render_template
from app.routes import chatbot
import os

app = Flask(__name__, static_folder="static", template_folder="static")
app.register_blueprint(chatbot)

@app.route("/")
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)
