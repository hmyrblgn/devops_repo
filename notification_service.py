from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

notifications = []

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.json
    if 'userId' not in data:
        return jsonify({"error": "userId is required"}), 400
    
    notifications.append(data)
    return jsonify({"message": "Notification sent!"}), 201

@app.route('/notifications/<user_id>', methods=['GET'])
def get_notifications(user_id):
    user_notifications = [n for n in notifications if n['userId'] == user_id]
    
    if not user_notifications:
        return jsonify({"error": "User ID not found"}), 404
    
    return jsonify(user_notifications), 200

@app.route('/form', methods=['GET'])
def notification_form():
    return render_template('notification_form.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
