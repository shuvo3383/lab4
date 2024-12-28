from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for rentals
rentals = []

@app.route('/api/v1/rental', methods=['POST'])
def create_rental():
    rental_data = request.json
    rentals.append(rental_data)
    return jsonify({"message": "Rental created successfully", "rental": rental_data}), 201

@app.route('/api/v1/rental', methods=['GET'])
def get_rentals():
    return jsonify(rentals)

if __name__ == '__main__':
    app.run(port=8060)
