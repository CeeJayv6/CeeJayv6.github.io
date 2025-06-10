from flask import Flask, request, jsonify, session, redirect

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Vulnerable users data
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

# Insecure profile endpoint with IDOR vulnerability
@app.route('/profile')
def profile():
    user_id = request.args.get('user_id')
    # No check if session user_id matches user_id in query
    if user_id in users:
        return jsonify({'profile': users[user_id]['profile']})
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

