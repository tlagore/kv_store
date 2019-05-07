from abc import ABC, abstractmethod

import pickle
import socket
import threading
import time

from kv_common.kv_message import KVMessage, KVMessageType
from kv_common.kv_state import KVState
from kv_common.kv_common import time_message
from kv_common.kv_socket import KVSocket

class KVListener(ABC):
    def __init__(self, id, name, port):
        self._port = port
        self._id = id
        self._name = name
        self._listening = False
        self._listen_lock = threading.Lock()

    def prep_socket(self, host, port):
        """ """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.bind((host, port))

        return sock

    def start_listening(self):
        try:
            self._socket = self.prep_socket("0.0.0.0", self._port)
            self._client_thread = threading.Thread(target=self._listen)
            self._listening = True

            self._client_thread.start()
        except socket.error as ex:
            print(time_message("Error initializing socket: {0}".format(type(ex).__name__)))


    def _listen(self):
        """Listen for a client"""

        try:
            while self._listening:
                with self._listen_lock:
                    self._socket.listen(5)
                (client, address) = self._socket.accept()
                clientThread = threading.Thread(target=self._worker, args=((client, address),))
                clientThread.start()
        except OSError:
            #expected error from controlled shutdown
            pass
        except Exception as ex:
            print(time_message("Unexpected exception occurred"))
            print(time_message(str(ex)))

        print(self.__str__())
        print("Exitting....")

    @abstractmethod
    def _worker(self, args):
        """Handle a client"""
        pass

    #@abstractmethod
    #def _handle_message(self, msg):
    #    """ abstract, handle a message received from a client """
    #    pass

    def __str__(self):
        return str("Listener {0}:({1}) listening on port {2}".format(self._name, self._id, self._port))

class KVSlaveListener(KVListener):
    def _worker(self, args):
        (client, address) = args

        sock = KVSocket(client)
        print("KVSlaveListener worker! {0}".format(address))
        self._listening = False

        try:
            print(time_message("Client connected"))
            msg = sock.recv_message()
            print("Client sends message with message type {0}".format(msg.message_type))
            resp = KVMessage(KVMessageType.ACK, "key1", "content1")
            sock.send_message(resp)
        except:
            print(time_message("Client disconnected: {0}".format(address[0])))

        with self._listen_lock:
            self._socket.shutdown(socket.SHUT_RDWR)
        self._socket.close()

class KVClientListener(KVListener):
    def _worker(self, args):
        (client, address) = args

        sock = KVSocket(client)
        print("KVClientListener worker! {0}".format(address))

        try:
            print(time_message("Client connected"))
            msg = sock.recv_message()
            print("Client sends message with message type {0}".format(msg.message_type))
            resp = KVMessage(KVMessageType.ACK, "key1", "content1")
            sock.send_message(resp)
        except:
            print(time_message("Client disconnected: {0}".format(address[0])))
            
        with self._listen_lock:
            self._socket.shutdown(socket.SHUT_RDWR)
        self._listening = False
        self._socket.close()
