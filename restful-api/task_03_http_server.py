#!/usr/bin/python3
"""
This module sets up a basic HTTP server using the http.server module.
It serves a simple API with endpoints for data, status, and info.
"""

import http.server
import json


class SimpleAPI(http.server.BaseHTTPRequestHandler):
    """
    A custom HTTP request handler class that processes GET requests
    and routes them to specific endpoints.
    """

    def do_GET(self):
        """
        Handle incoming GET requests and return appropriate HTTP
        responses and data based on the requested endpoint path.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dataset).encode("utf-8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info_data).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server_address = ("localhost", 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPI)
    httpd.serve_forever()
