import http.server
import socketserver

PORT = 8000  # You can change the port number here

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"serving at porty {PORT}")
    httpd.serve_forever()