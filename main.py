# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : main.py                 #
# ----------------------------------------------- #

import time

from flask import Flask, request


from handler import *

app = Flask(__name__)

def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp


@app.route("/", methods=["GET"])
def home():
    return "rodando", 200


@app.route("/heroku", methods=["POST"])
def notifier():
    try:
        if request.method == "POST":
            data = request.get_json()
            send_alert(data)
            return "Sent alert", 200

    except Exception as e:
        print("[X]", get_timestamp(), "Error:\n>", e)
        return "Error", 400
    
if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=5000)
