from kv_common.kv_message import KVMessage
from kv_common.kv_message import KVMessageType


kvmsg = KVMessage(KVMessageType.QUERY_TO_COMMIT, "key", "content")
print(kvmsg.serialize())

kvval = kvmsg.deserialze(kvmsg.serialize())

print(kvval.message_type)