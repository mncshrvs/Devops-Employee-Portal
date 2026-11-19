from flask import Flask, render_template, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Rahul Sharma", "role": "DevOps Engineer", "department": "Engineering"},
    {"id": 2, "name": "Priya Verma", "role": "Python Developer", "department": "Development"},
    {"id": 3, "name": "Amit Patel", "role": "Cloud Engineer", "department": "Infrastructure"},
    {"id": 4, "name": "Neha Singh", "role": "QA Engineer", "department": "Testing"}
]

@app.route("/")
def home():
    return render_template("index.html", employees=employees)

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200