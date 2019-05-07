import pickle
import struct
import sys

from kv_common.kv_common import time_message

class KVSocket:
    def __init__ (self, socket):
        self._socket = socket

    def send_message(self, message):
        """ serialize message & preface it with a header indicating the size of the message """
        messageBytes = pickle.dumps(message)

        messageLen = len(messageBytes)
        header = struct.pack("IIII", messageLen, messageLen, messageLen, messageLen)
            
        self._socket.sendall(header)
        self._socket.sendall(messageBytes)

            
    def recv_message(self):
        """ receives an encrypted message, decrypts it, and returns the message object """
    
        header = self.recvall(16) 
            
        messageSize = self.get_msg_size(header)
        messageBytes = self.recvall(messageSize)
        
        message = pickle.loads(messageBytes)
        return message

    def get_msg_size(self, header):
        """ unpacks header information and returns the length of the message """
        return struct.unpack("IIII", header)[0]
    
    def recvall(self, length):
        """ receives as many bytes as length from socket """
        data = bytes([])
        while len(data) < length:
            packet = self._socket.recv(length - len(data))
            if not packet:
                return None
            data+= packet
        return data 

    def close(self):
        try:
            self._socket.close()
        except:
            print(time_message("!! Error closing socket"), file=sys.stderr)
                                    
    def __del__(self):
        """destructor for chat client"""
        try:
            self._socket.close()
        except:
            print(time_message("Error closing socket"), file=sys.stderr)