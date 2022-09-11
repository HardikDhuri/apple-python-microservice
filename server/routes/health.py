
from flask import jsonify
from server import app

@app.route("/health")
def health():
    """health route"""
    state = {"status": "UP"}
    return jsonify(state)

@app.route("/answer")
def answer():
    """Answer route"""
    state = {"Apple is red": 100}
    return jsonify(state)

