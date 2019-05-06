from kv_slave.kv_slave import KeyValueSlave

def main():
    kvSlave = KeyValueSlave(1, 1024)
    print(kvSlave)

if __name__ == "__main__":
    main()