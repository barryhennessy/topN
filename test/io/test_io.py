from unittest import TestCase

from io import IO

__author__ = 'barryhennessy'


class TestIO(TestCase):
    # This assumes unit tests are being run from the project root directory
    valid_file = "test/io/valid_file.txt"
    invalid_file = "test/io/invalid_file.txt"

    def test_throws_if_path_non_readable(self):
        io = IO()
        with self.assertRaises(IOError):
            reader = io.read("path/that/doesn't/exist")
            for number in reader:
                pass

    def test_values_integers(self):
        io = IO()
        reader = io.read(self.valid_file)

        for number in reader:
            self.assertIsInstance(number, int)

    def test_non_int_raises_value_error(self):
        io = IO()
        reader = io.read(self.invalid_file)

        with self.assertRaises(ValueError):
            for number in reader:
                pass

    def test_reads_correct_ints(self):
        """Tests to ensure the correct numbers are returned

        Implicitly bound to the values in valid_file.txt. Make sure to keep the
        values in sync or use a different file if diverging often.
        """
        io = IO()
        reader = io.read(self.valid_file)

        self.assertItemsEqual([5, 6, 2, 4, 7, 232, 3], reader)
