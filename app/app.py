import os
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, response="Hello"):
        self.send_response(status_code)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))

    def do_GET(self):
        if self.path == "/hostname":
            self._set_response(response=os.uname().nodename)
        elif self.path == "/author":
            author = os.environ.get("AUTHOR", "Unknown")
            self._set_response(response=author)
        elif self.path == "/id":
            unique_id = os.environ.get("UUID", str(uuid.uuid4()))
            self._set_response(response=unique_id)
        else:
            self._set_response(status_code=404, response="Not Found")

def run(server_class=HTTPServer, handler_class=MyServer, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
