from typing import NamedTuple, BinaryIO


class TransformedData(NamedTuple):
    filename: str
    data: BinaryIO
