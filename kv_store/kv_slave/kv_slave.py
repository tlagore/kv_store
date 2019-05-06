import socket

class KeyValueSlave:
    def __init__(self, id, host, port):
        """ """ 
        self._id = id
        self._host = host
        self._port = port
    
    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((self._host, self._port))
            sock.sendall(bytes("Hello everyone! How are you today???", "utf-8"))

            received = str(sock.recv(1024), "utf-8")
            print(received)
        finally:
            sock.close()

    def __str__(self):
        return str("KeyValueSlave ({0}) master host: ({1}),running on port {2}".format(self._id, self._host, self._port))