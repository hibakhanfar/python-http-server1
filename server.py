from http.server import HTTPServer,BaseHTTPRequestHandler
import json
HOST = 'localhost'
PORT = 8080

class HelloHandler(BaseHTTPRequestHandler):

    def _send_json(self, status_code, payload):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def send_not_found(self):
        payload = {"error": "Endpoint not found"}
        self._send_json(404,payload)

    def do_GET(self):
        if(self.path == '/status'):
         payload = {
             "status": "running",
             "code": 200,
             "message": "Server is operational"
         }
         self._send_json(200,payload)
        else:
         self.send_not_found()

    def __getattr__(self, name):
        if name.startswith('do_'):
            return self.send_not_found
        raise AttributeError(name)

def main ():
    server=HTTPServer((HOST,PORT),HelloHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()

main()
