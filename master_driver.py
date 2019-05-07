from kv_master.kv_master import KVMaster

def main():
    server = KVMaster(2345, 3456)
    server.start()

if __name__ == "__main__":
    main()