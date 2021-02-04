import unittest

from base_repr import Base62, Base36


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.base62 = Base62(byteorder='little')
        self.base36 = Base36(byteorder='little')
        # (input, base62, base36)
        self.fixtures = (
            # int
            (
                (0, '0', '0'),
                (35, 'Z', 'Z'),
                (61, 'z', '1P'),
                (1234, 'Ju', 'YA'),
                (65535, 'H31', '1EKF')
            ),
            # bytes
            (
                (b"", '', ''),
                (b"\x00", '0', '0'),
                (b"\x01", '1', '1'),
                (b"\x00\x00\x01", 'H32', '1EKG'),
                (b"\xff\xff", 'H31', '1EKF'),
            ),
            # str
            (
                ('', '', ''),
                ('test', '28DbjY', 'WB6ZQS'),
                ('한글', 'eBkBTHSP', '1E62RJ104T'),
                ('日本語', 'uFJUvdgwsY5u', 'H5P7XQ4C7KKRFQ'),
            )
        )

    def test_int_to_repr(self):
        for data, out62, out36 in self.fixtures[0]:
            self.assertEqual(out62, self.base62.int_to_repr(data))
            self.assertEqual(out36, self.base36.int_to_repr(data))
            for base in (self.base62, self.base36):
                self.assertEqual(data, base.repr_to_int(base.int_to_repr(data)))

    def test_bytes_to_repr(self):
        for data, out62, out36 in self.fixtures[1]:
            self.assertEqual(out62, self.base62.bytes_to_repr(data))
            self.assertEqual(out36, self.base36.bytes_to_repr(data))
            for base in (self.base62, self.base36):
                self.assertEqual(data, base.repr_to_bytes(base.bytes_to_repr(data)))

    def test_str_to_repr(self):
        for data, out62, out36 in self.fixtures[2]:
            self.assertEqual(out62, self.base62.str_to_repr(data))
            self.assertEqual(out36, self.base36.str_to_repr(data))
            for base in (self.base62, self.base36):
                self.assertEqual(data, base.repr_to_str(base.str_to_repr(data)))

    def test_to_repr(self):
        for fixtures, func in zip(self.fixtures, ('int_to_repr', 'bytes_to_repr', 'str_to_repr')):
            for data, out62, out36 in fixtures:
                self.assertEqual(out62, self.base62.to_repr(data))
                self.assertEqual(out36, self.base36.to_repr(data))
                for base in (self.base62, self.base36):
                    self.assertEqual(base.to_repr(data), getattr(base, func)(data))


if __name__ == '__main__':
    unittest.main()
