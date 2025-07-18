from flask import Flask, render_template, jsonify
from pyorbital.orbital import Orbital
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/iss-location")
def iss_location():
    satellite = Orbital("ISS (ZARYA)")
    utc_now = datetime.utcnow()
    lon, lat, _ = satellite.get_lonlatalt(utc_now)
    return jsonify({
        "latitude": lat,
        "longitude": lon,
        "timestamp": utc_now.strftime('%Y-%m-%d %H:%M:%S UTC')
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6060)