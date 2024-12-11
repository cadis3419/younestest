from flask import Flask, request, jsonify


app = Flask(__name__)

# In-memory storage for simplicity
users = []

@app.route('/users', methods=['GET'])
def get_users():
    """
    Retrieve all users.
    """
    return jsonify({'users': users})

@app.route('/users', methods=['POST'])
def add_user():
    """
    Add a new user with a name and email.
    """
    user = request.json
    if 'name' not in user or 'email' not in user:
        return jsonify({'error': 'Name and email are required!'}), 400
    
    users.append(user)
    return jsonify({'message': 'User added successfully!', 'user': user}), 201

@app.route('/')
def home():
    """
    A welcome route.
    """
    return "Welcome to the User Directory App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1934)
