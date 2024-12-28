from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/manage/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/gateway/orders', methods=['GET'])
def get_orders():
    # Logic to retrieve orders from OrderService
    response = requests.get('http://orderservice:8060/orders')
    return jsonify(response.json()), response.status_code

@app.route('/gateway/users', methods=['GET'])
def get_users():
    # Logic to retrieve users from UserService
    response = requests.get('http://userservice:8050/users')
    return jsonify(response.json()), response.status_code

@app.route('/gateway/inventory', methods=['GET'])
def get_inventory():
    # Logic to retrieve inventory from WarehouseService
    response = requests.get('http://warehouseservice:8070/inventory')
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
