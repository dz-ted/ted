from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')

        if not message:
            return jsonify({'response': 'الرسالة فارغة'}), 400

        # استجابة تجريبية
        response = f"قلت: {message}"
        return jsonify({'response': response})
    
    except Exception as e:
        print("❌ خطأ في السيرفر:")
        traceback.print_exc()  # هذا يظهر الخطأ كاملاً في Render Logs
        return jsonify({'response': 'حدث خطأ داخلي في الخادم'}), 500
