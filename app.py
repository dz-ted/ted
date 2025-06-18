import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app)

API_KEY = "sk-9e4d66f85a1f4895aa8817096d68aa9c"  # ← ضع مفتاحك هنا
API_URL = "https://api.deepseek.com/v1/chat/completions"  # غيّره إذا كان مختلفًا

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')

        if not message:
            return jsonify({'response': 'الرسالة فارغة'}), 400

        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }

        payload = {
            "model": "deepseek-chat",  # ← أو النموذج الصحيح الذي توفره DeepSeek
            "messages": [
                {"role": "system", "content": "أنت مساعد ذكي يتحدث العربية."},
                {"role": "user", "content": message}
            ]
        }

        response = requests.post(API_URL, json=payload, headers=headers)

        if response.status_code == 200:
            result = response.json()
            reply = result["choices"][0]["message"]["content"]
            return jsonify({'response': reply})
        else:
            print("❌ خطأ من DeepSeek:", response.status_code, response.text)
            return jsonify({'response': 'فشل الاتصال بـ DeepSeek'}), 500

    except Exception as e:
        print("❌ خطأ داخلي:")
        traceback.print_exc()
        return jsonify({'response': 'حدث خطأ داخلي في الخادم'}), 500
