import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
        <html>
        <head><title>Android App Backend</title></head>
        <body>
        <h1>Android App Deployment Successful!</h1>
        <p>Backend is running on Render.</p>
        </body>
        </html>
        """)

port = int(os.environ.get("PORT", 10000))
server = HTTPServer(("0.0.0.0", port), Handler)
print(f"Server running on port {port}")
server.serve_forever()
