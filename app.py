import socket
import time
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    wait = request.args.get("wait", default=-1, type=int)
    if wait > 0:
        ms = wait / 1000
        time.sleep(ms)
    output = f"Hostname: {socket.gethostname()}<br/>"
    for k, v in request.headers:
        output += f"{k}: {v}<br/>"
    return output

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)