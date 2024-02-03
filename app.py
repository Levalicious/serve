import socket
import time
import random
import string
import os
from flask import Flask, request, make_response, session, render_template

app = Flask(__name__)
app.secret_key = "example_secret_key"

@app.route("/health")
def health():
    return ""

@app.route('/.well-known/acme-challenge/2PPZNvDNekU2sqSkRGc7tZ5ZQpowwF3BNi25IVBT_U4', methods=['GET', 'POST'])
def acme():
    return "2PPZNvDNekU2sqSkRGc7tZ5ZQpowwF3BNi25IVBT_U4.hTgoQkTb4svVt86kXP6zXU12ay5UaOwxreP2lScXWbw"

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
