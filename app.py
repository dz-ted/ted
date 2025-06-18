from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

DEEPSEEK_API_KEY = "sk-9e4d66f85a1f4895aa8817096d68aa9c"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "أنت مساعد ذكي يتحدث اللغة العربية، ساعد المستخدم بأجوبة دقيقة ومبسطة."},
                {"role": "user", "content": user_message}
            ]
        }

        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": f"خطأ في الخادم: {str(e)}"}), 500
