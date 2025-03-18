from flask import Flask
from flask_cors import CORS
import requests
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)

# List of services to ping
URLS = [
    "https://digibot.onrender.com",
    "https://live-service.onrender.com"
]

def ping_services():
    for url in URLS:
        try:
            requests.get(url)
        except requests.exceptions.RequestException as e:
            print(f"Error pinging {url}: {e}")

# Scheduler to run every 10 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(ping_services, 'interval', minutes=1)
scheduler.start()

@app.route("/")
def home():
    return "live-service is running!"
