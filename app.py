import socket
import time
import random
import string
import os
import ssl
from threading import Thread
from flask import Flask, request, make_response, session, render_template

app = Flask(__name__)
# app.secret_key = "example_secret_key"

@app.route("/health")
def health():
    return ""
    
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

def run_http():
    app.run(host='0.0.0.0', port=8080)

def run_https():
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('/etc/ssl/certs/tls.crt', '/etc/ssl/certs/tls.key')
    app.run(host='0.0.0.0', port=8443, ssl_context=context)

if __name__ == "__main__":
    http_thread = Thread(target=run_http)
    http_thread.start()
    https_thread = Thread(target=run_https)
    https_thread.start()
    http_thread.join()
    https_thread.join()
