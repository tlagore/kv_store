import pickle
import socket
import threading
import time

from kv_common.kv_message import KVMessage, KVMessageType
from kv_common.kv_state import KVState
from kv_common.kv_common import time_message
from kv_common.kv_socket import KVSocket
from kv_master.kv_listener import KVClientListener, KVSlaveListener

class KVMaster():
    def __init__(self, slave_port, client_port):
        self._client_port = client_port
        self._slave_port = slave_port

    def start(self):
        self._client_listener = KVClientListener(1, "client", self._client_port)
        self._client_listener.start_listening()
        self._slave_listener = KVClientListener(2, "slave", self._slave_port)
        self._slave_listener.start_listening()

        self._client_listener._client_thread.join()
        self._slave_listener._client_thread.join()