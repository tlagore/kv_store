from kv_master.kv_master import KeyValueMaster
import socketserver

def main():
    HOST, PORT = "localhost", 3000
    server = socketserver.TCPServer((HOST, PORT), KeyValueMaster)
    server.serve_forever()

if __name__ == "__main__":
    main()