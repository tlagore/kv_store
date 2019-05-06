from enum import Enum

class KVState(Enum):
    QUERY_TO_COMMIT = 0
    VOTE_NO = 1
    VOTE_YES = 2
    COMMIT = 3
    ROLLBACK = 4
    ACK = 5

