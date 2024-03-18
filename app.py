import socket
import time
import random
import string
import os
import ssl
from flask import Flask, request, make_response, session, render_template

app = Flask(__name__)
# app.secret_key = "example_secret_key"

@app.route("/health")
def health():
    return ""
    
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('/etc/ssl/certs/tls.crt', '/etc/ssl/certs/tls.key')
    app.run(host='0.0.0.0', port=8080, ssl_context=context)
