#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os.path as p
import re
import webbrowser
import http.server
import color_generator


# htmlTemplateName = 'single.html'
htmlTemplateName = 'palette.html'


with open(p.join(p.dirname(__file__), htmlTemplateName)) as file:
    template = file.read()


print("Modes:", ', '.join(color_generator.generation.generation_modes()))
color_mode = input("Mode: ")


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/':
            self.send_error(404)
            return

        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()

        response = re.sub(re.escape('{color}'), lambda *a: color_generator.generate(color_mode).hex, template)

        self.wfile.write(response.encode())


server = http.server.HTTPServer(('', 8080), RequestHandler)

if __name__ == '__main__':
    webbrowser.open('http://localhost:8080/', 2)
    server.serve_forever()
