from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # لتفادي مشاكل CORS من تطبيق Flutter

API_KEY = "sk-9e4d66f85a1f4895aa8817096d68aa9c"  # مفتاح DeepSeek الخاص بك
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
        response_data = response.json()
        reply = response_data["choices"][0]["message"]["content"]
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"response": f"حدث خطأ: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
