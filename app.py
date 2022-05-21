import socket
import time
import random
import string
from flask import Flask, request, make_response, session

app = Flask(__name__)
app.secret_key = "example_secret_key"

@app.route("/health")
def health():
    return ""

@app.route("/")
def home():
    wait = request.args.get("wait", default=-1, type=int)
    sticky = request.args.get("sticky", default=-1, type=int)

    output = f"Hostname: {socket.gethostname()}<br/>" 
    for k, v in request.headers:
        output += f"{k}: {v}<br/>"

    if "my_session" in session:
        output += f"Session: {session['my_session']} <br/>"
    else:
        session['my_session'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    resp = make_response(output)

    if wait > 0:
        ms = wait / 1000
        time.sleep(ms)
    
    return resp

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)