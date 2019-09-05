"""Test module.
"""
import os
import sys
import unittest

import main

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestAdd(unittest.TestCase):
    """Contains tests for add function.
    """

    def test_add_value(self):
        """Tests the return value of the add function.
        """
        self.assertEqual(main.add(2, 5), 7)
        self.assertEqual(main.add(52, 5), 57)
        self.assertEqual(main.add(3, 3), 6)
        self.assertEqual(main.add(-2, -5), -7)

    def test_add_raise(self):
        """Test the exception raises.
        """
        self.assertRaises(TypeError, main.add, 3, 'test')
        self.assertRaises(TypeError, main.add, 3, 'test')
        self.assertRaises(TypeError, main.add, 'test', 'test')
        self.assertRaises(TypeError, main.add, [], 'test')
        self.assertRaises(TypeError, main.add, [], True)

class TestSubtract(unittest.TestCase):
    """Contains tests for add function.
    """

    def test_subtract_value(self):
        """Tests the return value of the add function.
        """
        self.assertEqual(main.subtract(2, 5), -3)
        self.assertEqual(main.subtract(52, 5), 47)
        self.assertEqual(main.subtract(3, 3), 0)
        self.assertEqual(main.subtract(-2, -5), 3)

    def test_subtract_raise(self):
        """Test the exception raises.
        """
        self.assertRaises(TypeError, main.subtract, 3, 'test')
        self.assertRaises(TypeError, main.subtract, 3, 'test')
        self.assertRaises(TypeError, main.subtract, 'test', 'test')
        self.assertRaises(TypeError, main.subtract, [], 'test')
        self.assertRaises(TypeError, main.subtract, [], True)
