"""A minimal local HTTP server that replies 'Hello local server' to every GET request."""

from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello local server")


server = HTTPServer(('localhost', 3000), MyHandler)
print("Connected server successfully", server)
server.serve_forever()
