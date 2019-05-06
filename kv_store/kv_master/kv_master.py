import socketserver

class KeyValueMaster(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:", self.client_address[0])
        print(self.data)
        self.request.sendall(self.data.upper())


    def __str__(self):
        return str("KeyValueMaster listening on port {0}".format(self._port))