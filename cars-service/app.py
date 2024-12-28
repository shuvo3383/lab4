from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for cars
cars = [
    {
        "car_uid": "109b42f3-198d-4c89-9276-a7520a7120ab",
        "brand": "Mercedes Benz",
        "model": "GLA 250",
        "registration_number": "ЛО777Х799",
        "power": 249,
        "price": 3500,
        "availability": True
    }
]

@app.route('/api/v1/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

@app.route('/api/v1/cars', methods=['POST'])
def create_car():
    car_data = request.json
    cars.append(car_data)
    return jsonify({"message": "Car created successfully", "car": car_data}), 201

@app.route('/api/v1/cars/<string:car_uid>', methods=['PUT'])
def update_car(car_uid):
    car_data = request.json
    for car in cars:
        if car['car_uid'] == car_uid:
            car.update(car_data)
            return jsonify({"message": "Car updated successfully", "car": car}), 200
    return jsonify({"error": "Car not found"}), 404

@app.route('/api/v1/cars/<string:car_uid>', methods=['DELETE'])
def delete_car(car_uid):
    global cars
    cars = [car for car in cars if car['car_uid'] != car_uid]
    return jsonify({"message": "Car deleted successfully"}), 204

if __name__ == '__main__':
    app.run(port=8070)
