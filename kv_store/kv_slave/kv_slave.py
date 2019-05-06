import socket

class KeyValueSlave:
    def __init__(self, id, port):
        """ """ 
        self._id = id
        self._port = port

    def __str__(self):
        return str("KeyValueSlave ({0}) running on port {1}".format(self._id, self._port))