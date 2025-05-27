from flask import Flask, request, jsonify
import json
import os

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
        if not os.path.exists("today_sentence.json"):
            return jsonify({"error": "No sentence saved yet."}), 404
        with open("today_sentence.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

