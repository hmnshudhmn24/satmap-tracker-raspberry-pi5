# 🛰️ SatMap Tracker – Real-Time Satellite Tracker with Live Map UI (Raspberry Pi 5)

SatMap Tracker is a real-time satellite tracking dashboard built with Flask and Leaflet.js for Raspberry Pi 5. It visualizes the current location of the International Space Station (ISS) on a live OpenStreetMap-based world map.

## 🌍 Features

- Real-time ISS position fetched every 5 seconds
- Beautiful, interactive world map with ISS marker
- Timestamp display in UTC
- Works headlessly on Raspberry Pi 5 with browser display
- Built with Flask backend + Leaflet.js frontend

## 🧰 Tech Stack

- Python 3
- Flask
- PyOrbital (satellite tracking)
- Leaflet.js (frontend map)
- OpenStreetMap tiles

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/satmap-tracker-raspberry-pi5.git
cd satmap-tracker-raspberry-pi5
```

### 2. Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip
pip3 install flask pyorbital pytz
```

### 3. Run the Application

```bash
python3 app.py
```

Access the dashboard in your browser via:

```
http://<your-pi-ip>:6060
```

## 📡 How It Works

- The backend uses `pyorbital` to get the ISS position (lat/lon).
- The frontend (HTML/JS) renders a Leaflet map and places a satellite icon marker.
- Location is updated every 5 seconds with a timestamp.

## 🛠️ Optional Enhancements

- Add tracking for custom satellites using TLE data
- Show orbit trail using recent position logs
- Deploy in kiosk mode using Chromium for mirror-like display
