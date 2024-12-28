from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for orders
orders = []

@app.route('/manage/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({"orders": orders}), 200

@app.route('/orders', methods=['POST'])
def create_order():
    order_data = request.json
    if not order_data or 'item' not in order_data:
        return jsonify({"error": "Invalid input"}), 400
    orders.append(order_data)
    return jsonify({"message": "Order created successfully", "order": order_data}), 201

@app.route('/orders/<string:order_id>', methods=['PUT'])
def update_order(order_id):
    order_data = request.json
    if not order_data or 'item' not in order_data:
        return jsonify({"error": "Invalid input"}), 400
    for order in orders:
        if order['order_id'] == order_id:
            order.update(order_data)
            return jsonify({"message": "Order updated successfully", "order": order}), 200
    return jsonify({"error": "Order not found"}), 404

@app.route('/orders/<string:order_id>', methods=['DELETE'])
def delete_order(order_id):
    global orders
    orders = [order for order in orders if order['order_id'] != order_id]
    return jsonify({"message": "Order deleted successfully"}), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8060)
