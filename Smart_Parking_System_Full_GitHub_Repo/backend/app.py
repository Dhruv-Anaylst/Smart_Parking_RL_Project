
from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)
slots = np.zeros(10)

@app.route("/status")
def status():
    return jsonify(slots.tolist())

@app.route("/recommend")
def recommend():
    free = np.where(slots == 0)[0]
    return jsonify({"slot": int(free[0]) if len(free) else -1})

@app.route("/park/<int:slot>")
def park(slot):
    if slots[slot] == 0:
        slots[slot] = 1
        return jsonify({"message": "Parking Confirmed"})
    return jsonify({"message": "Occupied"})

@app.route("/analytics")
def analytics():
    return jsonify({
        "total_slots": len(slots),
        "occupied": int(np.sum(slots)),
        "free": int(len(slots)-np.sum(slots))
    })

app.run(host="0.0.0.0", port=5000)
