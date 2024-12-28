from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = []

@app.route('/manage/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users}), 200

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    if not user_data or 'name' not in user_data:
        return jsonify({"error": "Invalid input"}), 400
    users.append(user_data)
    return jsonify({"message": "User created successfully", "user": user_data}), 201

@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    if not user_data or 'name' not in user_data:
        return jsonify({"error": "Invalid input"}), 400
    for user in users:
        if user['user_id'] == user_id:
            user.update(user_data)
            return jsonify({"message": "User updated successfully", "user": user}), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['user_id'] != user_id]
    return jsonify({"message": "User deleted successfully"}), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)
