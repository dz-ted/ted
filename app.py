from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # يسمح بالوصول من أي مصدر (مثل Flutter)

@app.route('/')
def home():
    return 'خادم نفسك AI يعمل ✅'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    # رد افتراضي بسيط – يمكن ربطه بنموذج ذكاء اصطناعي لاحقًا
    if user_message.strip() == '':
        return jsonify({'response': 'الرسالة فارغة. من فضلك اكتب شيئاً 😊'})
    
    # رد عشوائي أو من نموذج
    response = f'لقد قلت: "{user_message}". شكرًا على مشاركتك 🌟'
    return jsonify({'response': response})
