
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

@app.route("/nothing")
def nothing():
    """nothing route"""
    state = {"status":"Kuch ni milega yaha.... isliye nothing route h"}
    return jsonify(state)

