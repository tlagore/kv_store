from enum import Enum

class KVMessageType(Enum):
    QUERY_TO_COMMIT = 0
    VOTE = 1
    COMMIT = 2
    ROLLBACK = 3
    ACK = 4    

class KVMessage:
    def __init__(self, messageType, key, content):
        self.message_type = messageType
        self.key = key
        self.content = content