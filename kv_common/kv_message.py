from enum import Enum

class KVMessageType(Enum):
    QUERY_TO_COMMIT = 0
    VOTE = 1
    COMMIT = 2
    ROLLBACK = 3
    ACK = 4
    GET = 5
    PUT = 6
    DEL = 7

class KVMessage:
    def __init__(self, messageType, key, value):
        if not isinstance(messageType, KVMessageType):
            raise KVMessageException("message type must be of type KVMessageType")

        self.message_type = messageType

        if (self.message_type == KVMessageType.PUT and (value == None or key == None)):
            raise KVMessageException("PUT operation requires a key and a value")

        self.key = key
        self.value = value

    def __str__(self):
        return str("KVMessage:: Type: {} - key({}) : value({})".format(self.message_type, self.key, self.value))

class KVMessageException(Exception):
    pass