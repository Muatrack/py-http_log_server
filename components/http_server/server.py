
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
from http.server import BaseHTTPRequestHandler

routers = [
    '/v1/api/log'
]

class HttpSerReqHandle(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def _do_get_process_gateway(self):
        print("[ Got requestpath ]%s" % self.path )
        print("[ Got preset path ]%s" % routers[0] )
        if(self.path!=routers[0]):
            self.send_response(200, 'Got it')
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"val":"^^^"}')
            return

        self.send_response(200, 'Got it')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"val":"<<<"}')

    def _do_post_process_gateway(self):
        print("[ Got requestpath ]%s" % self.path )
        print("[ Got preset path ]%s" % routers[0] )
        if(self.path!=routers[0]):
            self.send_response(200, 'Got it')
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"val":"^^^"}')
            return

        self.send_response(200, 'Got it')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"val":"<<<"}')


    def do_GET(self):
        self._do_get_process_gateway()

    
    def do_POST(self):
        self._do_post_process_gateway()

def start(host:str='0.0.0.0',port:int=8000):
    bindAddr=(host, port)
    ser = HTTPServer(bindAddr, HttpSerReqHandle)
    print('Http server running at %s %d' % (host, port))
    ser.serve_forever()

if __name__ == "__main__":
    start()