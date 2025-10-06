#!/usr/bin/python3
"""
Simple HTTP server using http.server module
"""
import http.server
import socketserver
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """Simple HTTP request handler"""
    
    def do_GET(self):
        """Handle GET requests"""
        pass


def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    """Run the HTTP server"""
    pass


if __name__ == "__main__":
    run()