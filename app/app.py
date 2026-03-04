import http.server
import socketserver

PORT = 8080  # You can change the port number here

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"serving at port {PORT}")
    httpd.serve_forever()
