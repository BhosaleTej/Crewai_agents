
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
def divitiontionds(a,b,e):
    'addiation of tthr numbers'
    c = a * e
    return c

def multipliction(a,b):
    'multiplication of two numbers'
    c = a * b
    return c

def fact(n):
    factorial = n * fact(n-1)
    return factorial