import socket
import time
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def home():
    wait = request.args.get("wait", default=-1, type=int)
    sticky = request.args.get("sticky", default=-1, type=int)

    output = f"Hostname: {socket.gethostname()}<br/>"
    for k, v in request.headers:
        output += f"{k}: {v}<br/>"
    resp = make_response(output)

    if wait > 0:
        ms = wait / 1000
        time.sleep(ms)
    
    if sticky > 0:
        resp.set_cookie("sticky", "any_value", max_age=sticky)
    
    return resp

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)