from kv_slave.kv_slave import KeyValueSlave

def main():
    kvSlave = KeyValueSlave(1, "127.0.0.1", 3000)
    kvSlave.start()

if __name__ == "__main__":
    main()