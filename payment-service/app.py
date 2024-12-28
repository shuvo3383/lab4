from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for payments
payments = []

@app.route('/api/v1/payment', methods=['POST'])
def create_payment():
    payment_data = request.json
    payments.append(payment_data)
    return jsonify({"message": "Payment created successfully", "payment": payment_data}), 201

@app.route('/api/v1/payment', methods=['GET'])
def get_payments():
    return jsonify(payments)

if __name__ == '__main__':
    app.run(port=8050)
