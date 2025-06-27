from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import os

# Change to the directory where server.py is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create HTTP server
httpd = HTTPServer(('0.0.0.0', 8443), SimpleHTTPRequestHandler)

# Create SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

# Wrap socket with SSL
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving HTTPS on port 8443...")
httpd.serve_forever()