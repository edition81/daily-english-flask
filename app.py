from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    with open("today_sentence.json", "w") as f:
        json.dump(data, f)
    return jsonify({"status": "success"}), 200

@app.route('/today', methods=['GET'])
def get_today_sentence():
    try:
        with open("today_sentence.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "No sentence found."}), 404
