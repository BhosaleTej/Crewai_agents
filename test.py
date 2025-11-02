
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
ngrok_url = os.getenv("NGROK_URL")

app = FastAPI()

@app.get("/info")
def get_info():
    return {"public_url": ngrok_url}


'this is second push'
