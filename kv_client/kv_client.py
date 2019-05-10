import socket
from kv_common.kv_message import KVMessage, KVMessageType
from kv_common.kv_socket import KVSocket

class KVClient:
    def __init__(self, id, host, port):
        """ """ 
        self._id = id
        self._host = host
        self._port = port
    
    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((self._host, self._port))
            msg = KVMessage(KVMessageType.PUT, "key", "content")

            self._master_socket = KVSocket(sock)
            self._master_socket.send_message(msg)

            resp = self._master_socket.recv_message()
            print("Master says {0}".format(resp.message_type))

        finally:
            sock.close()

    def __str__(self):
        return str("KVClient ({0}) master host: ({1}),running on port {2}".format(self._id, self._host, self._port))