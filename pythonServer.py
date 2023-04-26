import http.server
import socketserver

#code to run html file on http server
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


Handler = MyRequestHandler
PORT = 8080

#looks for connections on port 8080
with socketserver.TCPServer(('0.0.0.0', PORT), Handler) as server:
    print('Server started on port', PORT)
    server.serve_forever()
