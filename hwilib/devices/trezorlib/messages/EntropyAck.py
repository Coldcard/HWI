# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class EntropyAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 36

    def __init__(
        self,
        entropy: bytes = None,
    ) -> None:
        self.entropy = entropy

    @classmethod
    def get_fields(cls):
        return {
            1: ('entropy', p.BytesType, 0),
        }
