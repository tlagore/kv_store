from kv_master.kv_master import KVMaster

def main():
    HOST, PORT = "localhost", 3000
    server = KVMaster(2345, 3456)
    server.start_listen_slaves()

if __name__ == "__main__":
    main()