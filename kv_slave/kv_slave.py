import socket
from kv_common.kv_message import KVMessage, KVMessageType
import pickle

class KVSlave:
    def __init__(self, id, host, port):
        """ """ 
        self._id = id
        self._host = host
        self._port = port
    
    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((self._host, self._port))
            msg = KVMessage(KVMessageType.QUERY_TO_COMMIT, "key", "content")

            sock.sendall(pickle.dumps(msg))

            #received = str(sock.recv(1024), "utf-8")
            #print(received)
        finally:
            sock.close()

    def __str__(self):
        return str("KVSlave ({0}) master host: ({1}),running on port {2}".format(self._id, self._host, self._port))