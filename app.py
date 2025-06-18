from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

HF_TOKEN = "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"
HF_API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/deepseek-coder-6.7b-instruct"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"response": "يرجى إدخال رسالة."})

    payload = {
        "inputs": f"### User:\n{user_input}\n\n### Assistant:\n",
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7,
        }
    }

    response = requests.post(HF_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()[0]["generated_text"]
        reply = result.split("### Assistant:\n")[-1].strip()
        return jsonify({"response": reply})
    else:
        return jsonify({"response": "حدث خطأ أثناء التواصل مع نموذج الذكاء الاصطناعي."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)