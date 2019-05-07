import pickle
import socket
import threading

from kv_common.kv_message import KVMessage, KVMessageType
from kv_common.kv_state import KVState
from kv_common.kv_common import time_message
from kv_common.kv_socket import KVSocket

class KVMaster():
    def __init__(self, slave_port, client_port):
        self._client_port = client_port
        self._slave_port = slave_port

    def start_listen_slaves(self):
        try:
            self._slave_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._slave_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # 0.0.0.0 binds to all available interfaces
            self._slave_socket.bind(("0.0.0.0", self._slave_port))

            self._listen_slaves()
        except socket.error as ex:
            print(time_message("Error initializing socket: {0}".format(type(ex).__name__)))

    def _listen_slaves(self):
        """Listen for a client"""

        while True:
            self._slave_socket.listen(5)
            (client, address) = self._slave_socket.accept()
            clientThread = threading.Thread(target=self._slave_worker, args=((client, address),))
            clientThread.start()

    def _slave_worker(self, args):
        """Handle a client"""
        (client, address) = args
        sock = KVSocket(client)
        
        try:
            print(time_message("Client connected"))
            msg = sock.recv_message()
            print("Client sends message with message type {0}".format(msg.message_type))
            resp = KVMessage(KVMessageType.ACK, "key1", "content1")
            sock.send_message(resp)
        except:
            print(time_message("Client disconnected: {0}".format(address[0])))

    #def handle(self):
    #    data = self.request.recv(1024).strip()
    #    try:
    #        msg = pickle.loads(data)
    #        self.handle_message(msg)
    #    except:
    #        print("Error trying to deserialize message")

    def handle_message(self, msg):
        try:
            if(msg.message_type == KVMessageType.QUERY_TO_COMMIT):
                print("Query to commit")
                pass
            elif(msg.message_type == KVMessageType.VOTE):
                print("vote")
                pass
            elif(msg.message_type == KVMessageType.COMMIT):
                print("commit")
                pass
            elif(msg.message_type == KVMessageType.ROLLBACK):
                print("rollback")
                pass
            else:
                print("Message type not supported")
        except Exception as ex:
            print(ex)

    def __str__(self):
        return str("KeyValueMaster listening on port {0}".format(self._port))