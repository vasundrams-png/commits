print("Backend initialization")
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend Running"

app.run(debug=True)
