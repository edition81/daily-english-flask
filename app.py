from flask import Flask, request, jsonify
import json
import os
import random

app = Flask(__name__)

# 📥 문장 리스트 저장
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if isinstance(data, list):
        with open("today_sentences.json", "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return jsonify({"status": "✅ 전체 문장 저장 완료", "count": len(data)}), 200
    else:
        return jsonify({"error": "❌ 리스트 형식이 아닙니다."}), 400

# 📤 랜덤 문장 10개 반환
@app.route('/today', methods=['GET'])
def get_random_sentences():
    if not os.path.exists("today_sentences.json"):
        return jsonify({"error": "❌ 저장된 문장이 없습니다."}), 404
    with open("today_sentences.json", "r", encoding='utf-8') as f:
        sentences = json.load(f)
    if not isinstance(sentences, list) or len(sentences) == 0:
        return jsonify({"error": "❌ 유효한 문장 리스트가 아닙니다."}), 400

    sample = random.sample(sentences, min(10, len(sentences)))  # 최대 10개 선택
    return jsonify(sample)

