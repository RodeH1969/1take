from flask import Flask
from flask_sslify import SSLify
import os

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/')
def serve_index():
    return open('index.html').read()

@app.route('/static/<path:path>')
def serve_static(path):
    return open(f'static/{path}', 'rb').read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))