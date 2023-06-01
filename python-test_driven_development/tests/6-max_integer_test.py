#!/usr/bin/python3
"""unittests for 6-max_integer"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """class for testing 6-max_integer"""
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([4, 7, 3]), 7)

    def test_one_negative(self):
        self.assertEqual(max_integer([2, 3, -5, 4]), 4)

    def test_all_negative(self):
        self.assertEqual(max_integer([-5, -4, -2, -3, -1, -6]), -1)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty(self):
        self.assertEqual(max_integer(), None)
