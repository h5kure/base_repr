import hashlib
import unittest
from base_repr import int_to_repr, repr_to_int, bytes_to_repr, repr_to_bytes, str_to_repr, repr_to_str
from base_repr.functions import to_repr


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.fixtures = (
            # int
            (1, 1234, 15, 122),
            # bytes
            (
                b"\x01",
                bytes([1, 2, 3, 4]),
                hashlib.sha256("Hello World".encode()).digest(),
            ),
            # str
            (
                ""
                "Hello",
                "World"
            )
        )

    def test_int_to_repr(self):
        self.assertEqual('0', int_to_repr(0))
        self.assertEqual(0, repr_to_int('0'))
        for i in self.fixtures[0]:
            self.assertEqual(i, repr_to_int(int_to_repr(i)))

    def test_bytes_to_repr(self):
        self.assertEqual('', bytes_to_repr(b''))
        self.assertEqual(b'', repr_to_bytes(''))
        self.assertEqual('0', bytes_to_repr(bytes([0])))
        self.assertEqual(bytes([0]), repr_to_bytes('0'))
        for b in self.fixtures[1]:
            self.assertEqual(b, repr_to_bytes(bytes_to_repr(b)))

    def test_str_to_repr(self):
        self.assertEqual('', str_to_repr(''))
        self.assertEqual('', repr_to_str(''))
        for s in self.fixtures[2]:
            self.assertEqual(s, repr_to_str(str_to_repr(s)))

    def test_to_repr(self):
        for i in self.fixtures[0]:
            self.assertEqual(to_repr(i), int_to_repr(i))

        for b in self.fixtures[1]:
            self.assertEqual(to_repr(b), bytes_to_repr(b))

        for s in self.fixtures[2]:
            self.assertEqual(to_repr(s), str_to_repr(s))


if __name__ == '__main__':
    unittest.main()
