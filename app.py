from flask import Flask
from pytz import timezone 
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/time")
def print_time():
    date = str(datetime.now(timezone("Asia/Kolkata")))
    time = date[10:19]
    return time

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)