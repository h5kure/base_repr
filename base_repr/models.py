import sys
from typing import Union

from .functions import int_to_repr, repr_to_int, bytes_to_repr, repr_to_bytes, str_to_repr, repr_to_str, to_repr


class BaseRepr(object):
    """Base class"""
    def __init__(self, *, base: int = 2, padding: int = 0, byteorder: str = sys.byteorder, encoding: str = 'utf-8'):
        self.base = base
        self.padding = padding
        self.byteorder = byteorder
        self.encoding = encoding

    def int_to_repr(self, number: int) -> str:
        return int_to_repr(number, base=self.base, padding=self.padding)

    def repr_to_int(self, string_: str) -> int:
        return repr_to_int(string_, base=self.base)

    def bytes_to_repr(self, bytes_: bytes) -> str:
        return bytes_to_repr(bytes_, base=self.base, padding=self.padding, byteorder=self.byteorder)

    def repr_to_bytes(self, string_: str) -> bytes:
        return repr_to_bytes(string_, base=self.base, byteorder=self.byteorder)

    def str_to_repr(self, string_: str) -> str:
        return str_to_repr(string_, base=self.base, padding=self.padding, byteorder=self.byteorder, encoding=self.encoding)

    def repr_to_str(self, string_: str) -> str:
        return repr_to_str(string_, base=self.base, byteorder=self.byteorder, encoding=self.encoding)

    def to_repr(self, value: Union[int, bytes, str]) -> str:
        return to_repr(value, base=self.base, padding=self.padding, byteorder=self.byteorder, encoding=self.encoding)


class Base62(BaseRepr):
    def __init__(self, *, padding: int = 0, byteorder: str = sys.byteorder, encoding: str = 'utf-8'):
        super().__init__(base=62, padding=padding, byteorder=byteorder, encoding=encoding)


class Base36(BaseRepr):
    def __init__(self, *, padding: int = 0, byteorder: str = sys.byteorder, encoding: str = 'utf-8'):
        super().__init__(base=36, padding=padding, byteorder=byteorder, encoding=encoding)
