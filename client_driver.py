from kv_client.kv_client import KVClient

def main():
    kvSlave = KVClient(1, "127.0.0.1", 3456)
    kvSlave.start()

if __name__ == "__main__":
    main()