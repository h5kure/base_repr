import unittest
from timeit import Timer


class TestCase(unittest.TestCase):
    def test_performance_functions(self):
        cmds = (
            ("int_to_repr(1234, base=62)", "from base_repr import int_to_repr"),
            ("repr_to_int('Ju', base=62)", "from base_repr import repr_to_int"),
            ("bytes_to_repr(bytes([255]), base=62)", "from base_repr import bytes_to_repr"),
            ("repr_to_bytes('47', base=62)", "from base_repr import repr_to_bytes"),
            ("str_to_repr('test', base=62)", "from base_repr import str_to_repr"),
            ("repr_to_str('28DbjY', base=62)", "from base_repr import repr_to_str"),
        )
        number = 1_000_000
        for cmd, setup in cmds:
            timer = Timer(cmd, setup=setup)
            print(f"Time {cmd} took to run {number:,d} times:", timer.timeit(number))


if __name__ == '__main__':
    unittest.main()
