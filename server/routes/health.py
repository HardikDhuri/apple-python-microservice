
from flask import jsonify
from server import app

@app.route("/health")
def health():
    """health route"""
    state = {"status": "UP"}
    return jsonify(state)

@app.route('/answer/<number>')
def CheckAnswerToLifeTheUniverseAndEverything(number):
    content = {
        'statement': 'The Answer to Life the Universe and Everything is ' + number + '.',
        'check': 'The statement is ' + str(number == '42') + '!'
    }
    return jsonify(content)

@app.route("/nothing")
def nothing():
    """nothing route"""
    state = {"status":"Kuch ni milega yaha.... isliye nothing route h"}
    return jsonify(state)

