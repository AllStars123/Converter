from http.server import HTTPServer

from server import HTTPHandler


serv = HTTPServer(('localhost', 80), HTTPHandler)
serv.serve_forever()
