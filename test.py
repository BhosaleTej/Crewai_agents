
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
def divitionios(a,b,e):
    'addiation of tthr numbers'
    c = a / b
    return c

def addition(a,b):
    'addtion of numbrs'
    c = a+b
    return c

def multiplication(a,b):
    'mul of numbers'
    c = a * b
    return c