from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/appointments_db"
mongo = PyMongo(app)

@app.route("/save_appointment", methods=["POST"])
def save_appointment():
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "date", "time", "contact")):
        return jsonify({"error": "Missing required fields"}), 400
    
    appointment = {
        "name": data["name"],
        "date": data["date"],
        "time": data["time"],
        "contact": data["contact"]
    }
    
    mongo.db.appointments.insert_one(appointment)
    return jsonify({"message": "Appointment booked successfully"}), 201

@app.route("/appointments", methods=["GET"])
def get_appointments():
    appointments = list(mongo.db.appointments.find({}, {"_id": 0}))
    return jsonify(appointments)

if __name__ == "__main__":
    app.run(debug=True)