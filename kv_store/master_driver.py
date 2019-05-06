from kv_master.kv_master import KVMaster
import socketserver

def main():
    HOST, PORT = "localhost", 3000
    server = KVMaster(2345, 3456)
    server.start_listen_slaves()
    #server = socketserver.TCPServer((HOST, PORT), KVMaster)
    #server.serve_forever()

if __name__ == "__main__":
    main()