
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
ngrok_url = os.getenv("NGROK_URL")

app = FastAPI()

@app.get("/info")
def get_info():
    return {"public_url": ngrok_url}

# for testing of webhook trigger
# for second testing of webhook trigger
# for third testing of webhook trigger after stash

#addition function
def add(a,b):
    return a+b