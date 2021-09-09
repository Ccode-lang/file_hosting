import os
import http.server
import socketserver
os.chdir("files")
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as http:
    print("server at port", PORT)
    http.serve_forever()