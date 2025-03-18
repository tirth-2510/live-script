from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# List of services to ping
URLS = [
    "https://digibot.onrender.com",
    "https://live-script.onrender.com"
]

def ping_services():
    for url in URLS:
        try:
            requests.get(url)
        except requests.exceptions.RequestException:
            pass
            
scheduler = BackgroundScheduler()
scheduler.add_job(ping_services, 'interval', minutes=10)
scheduler.start()

@app.get("/")
def home():
    return {"message": "live-service is running!"}
