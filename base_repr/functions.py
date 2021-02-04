import string
import sys
from typing import Union

DIGITS = string.digits + string.ascii_uppercase + string.ascii_lowercase
DIGITS_INDICES = {char: index for index, char in enumerate(DIGITS)}
MIN_BASE = 2
MAX_BASE = len(DIGITS)


def _check_base(base: int):
    if base > MAX_BASE:
        raise ValueError("Cannot handle more than {} bases.".format(MAX_BASE))
    elif base < MIN_BASE:
        raise ValueError("Cannot handle less than {} bases.".format(MIN_BASE))


def int_to_bytes(number: int, *, byteorder: str = sys.byteorder) -> bytes:
    """
    convert integer to bytes
    :param number: integer
    :type number: int
    :param byteorder: determines reverse bytes or not.
    :type byteorder: str
    :return: bytes converted from passed integer
    :rtype: bytes
    """
    buffer = bytearray()
    while number:
        buffer.append(number & 0xFF)
        number //= 256
    if byteorder == 'big':
        buffer.reverse()
    return bytes(buffer) or bytes([0])


def int_to_repr(number: int, *, base: int = 2, padding: int = 0) -> str:
    """
    Return a string representation of a number in the given `base` system.
    :param number: integer to convert.
    :type number: int
    :param base: base number
    :type base: int
    :param padding: fill the remaining digits with zeros. default 0 means no padding.
    :type padding: int
    :return: string representation of `number` in the given `base` system.
    :rtype: str
    """
    _check_base(base)

    result = []
    abs_number = abs(number)
    while abs_number:
        abs_number, remainder = divmod(abs_number, base)
        result.append(DIGITS[remainder])

    if len(result) < padding:
        result.append('0' * (padding - len(result)))

    if number < 0:
        result.append('-')

    return ''.join(reversed(result or '0'))


def repr_to_int(string_: str, *, base: int = 2) -> int:
    """
    Return a number from string representation of the given base system.
    :param string_: string representation in the `base` system.
    :type string_: str
    :param base: base number
    :type base: int
    :return: number from `string_` representation in the given `base` system.
    :rtype: int
    """
    _check_base(base)

    number = 0
    for index, digit in enumerate(reversed(string_)):
        number += DIGITS_INDICES[digit] * (base ** index)

    return number


def bytes_to_repr(bytes_: bytes, *, base: int = 2, padding: int = 0, byteorder: str = sys.byteorder) -> str:
    """
    Return a string representation of a bytes in the given `base` system.
    :param bytes_: bytes to convert.
    :type bytes_: bytes
    :param base: base number
    :type base: int
    :param padding: fill the remaining digits with zeros. default 0 means no padding.
    :type padding: int
    :param byteorder: determines the byte order used to represent the integer.
    :type byteorder: str
    :return: string representation of `bytes_` in the given `base` system.
    :rtype:str
    """
    if not bytes_:
        return ''
    return int_to_repr(int.from_bytes(bytes_, byteorder), base=base, padding=padding)


def repr_to_bytes(string_: str, *, base: int = 2, byteorder: str = sys.byteorder) -> bytes:
    """
    Return a bytes from a string representation of the given base system.
    :param string_: string representation in the `base` system.
    :type string_: str
    :param base: base number
    :type base: int
    :param byteorder: determines reverse bytes or not.
    :type byteorder: str
    :return: bytes from a `string_` representation in the given `base` system.
    :rtype: bytes
    """
    if not string_:
        return b''
    return int_to_bytes(repr_to_int(string_, base=base), byteorder=byteorder)


def str_to_repr(string_: str,
                *,
                base: int = 2,
                padding: int = 0,
                byteorder: str = sys.byteorder,
                encoding: str = 'utf-8') -> str:
    """
    Return a string representation of string in the given `base` system.
    :param string_: string to convert
    :type string_: str
    :param base: base number
    :type base: int
    :param padding: fill the remaining digits with zeros. default 0 means no padding.
    :type padding: int
    :param byteorder: determines the byte order used to represent the integer.
    :type byteorder: str
    :param encoding: encoding to encode string to bytes
    :type encoding: str
    :return: string representation of `string_` in the given `base` system.
    :rtype: str
    """
    return bytes_to_repr(string_.encode(encoding), base=base, padding=padding, byteorder=byteorder)


def repr_to_str(string_: str, *, base: int = 2, byteorder: str = sys.byteorder, encoding: str = 'utf-8') -> str:
    """
    Return a string from a string representation in the given base system.
    :param string_: string representation in the `base` system.
    :type string_: str
    :param base: base number
    :type base: int
    :param byteorder: determines reverse bytes or not
    :type byteorder:
    :param encoding: encoding to decode string from bytes
    :type encoding: str
    :return: string from a `string_` representation in the given `base` system.
    :rtype: str
    """
    return repr_to_bytes(string_, base=base, byteorder=byteorder).decode(encoding)


def to_repr(value: Union[int, bytes, str], *,
            base: int = 2,
            padding: int = 0,
            byteorder: str = sys.byteorder,
            encoding: str = 'utf-8') -> str:
    if isinstance(value, str):
        return str_to_repr(value, base=base, padding=padding, byteorder=byteorder, encoding=encoding)

    if isinstance(value, bytes):
        return bytes_to_repr(value, base=base, padding=padding, byteorder=byteorder)

    if isinstance(value, int):
        return int_to_repr(value, base=base, padding=padding)

    raise TypeError(f"Unsupported value type: {type(value)}")
