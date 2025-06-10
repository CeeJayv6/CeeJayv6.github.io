
from flask import Flask, request, jsonify, session, redirect

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Secure users data
users = {
    'alice': {'password': 'password123', 'profile': 'Alice’s profile data'},
    'bob': {'password': 'mypassword', 'profile': 'Bob’s profile data'},
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users and users[username]['password'] == password:
        session['user_id'] = username
        return jsonify({'message': 'Logged in'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# Secure profile endpoint - enforces session user_id
@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'Unauthorized'}), 401
    if user_id in users:
        return jsonify({'profile': users[user_id]['profile']})
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
