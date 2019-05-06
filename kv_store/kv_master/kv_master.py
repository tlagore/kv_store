import socketserver
import pickle

class KVMaster(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        try:
            msg = pickle.loads(data)
            self.handle_message(msg)
        except:
            print("Error trying to deserialize message")

    def handle_message(self, msg):
        print(msg.message_type)
 
    def __str__(self):
        return str("KeyValueMaster listening on port {0}".format(self._port))