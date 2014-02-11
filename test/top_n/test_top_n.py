from unittest import TestCase

from top_n import TopN

__author__ = 'barryhennessy'


class TestTopN(TestCase):
    """Tests the TopN class"""

    def test_negative_number_instantiation_raises_value_error(self):
        with self.assertRaises(ValueError):
            top = TopN(-10)

    def test_0_n_instantiation_raises_value_error(self):
        with self.assertRaises(ValueError):
            top = TopN(0)

    def test_string_rep_int_operates_correctly(self):
        top = TopN("2")

        top.push(1)
        top.push(2)
        top.push(3)

        top_n = top.get_top_n()

        self.assertListEqual(top_n, [3, 2])
        self.assertListEqual(top_n, [3, 2])

    def test_invalid_int_raises_type_error(self):
        with self.assertRaises(TypeError):
            top = TopN({123})

    def test_get_top_n_returns_list(self):
        top = TopN(2)
        top.push(1)
        top.push(2)

        top_n = top.get_top_n()
        self.assertIsInstance(top_n, list)

    def test_top_n_in_sorted_order(self):
        top = TopN(3)

        for number in range(20, 41):
            top.push(number)

        top_n = top.get_top_n()

        sorted_top_n = top_n[:]
        sorted_top_n.sort(reverse=True)

        self.assertItemsEqual(top_n, sorted_top_n)

    def test_top_n_no_greater_than_specified(self):
        n = 5
        top = TopN(n)

        for number in range(1, 11):
            top.push(number)

        top_n = top.get_top_n()

        self.assertEqual(len(top_n), n)

    def test_captures_top_5_of_10_correctly(self):
        top = TopN(5)

        for number in range(1, 11):
            top.push(number)

        top_n = top.get_top_n()

        self.assertListEqual(top_n, [10, 9, 8, 7, 6])

    def test_negative_numbers_handled_correctly(self):
        top = TopN(5)

        for number in range(-10, 3):
            top.push(number)

        top_n = top.get_top_n()

        self.assertListEqual(top_n, [2, 1, 0, -1, -2])

    def test_all_input_same_number(self):
        top = TopN(2)

        for number in [5] * 100:
            top.push(number)

        top_n = top.get_top_n()

        self.assertListEqual(top_n, [5, 5])

    def test_input_less_than_n(self):
        top = TopN(100)

        for number in range(1, 5):
            top.push(number)

        top_n = top.get_top_n()

        self.assertListEqual(top_n, [4, 3, 2, 1])

    def test_get_top_and_continue(self):
        top = TopN(5)

        for number in range(1, 11):
            top.push(number)

        top_n = top.get_top_n()

        for number in [20, 25]:
            top.push(number)

        top_n = top.get_top_n()

        self.assertListEqual(top_n, [25, 20, 10, 9, 8])