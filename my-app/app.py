# This is the Flask app for the website

from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis container
db = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    # Increment visitor counter in Redis
    visitor_count = db.incr('visitor_count')
    return f"Welcome to the website! You are visitor number {visitor_count}."

# Needs to run on port 5005
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
