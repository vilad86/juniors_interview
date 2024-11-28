import unittest

from task1.solution import (sum_float,
                            invert_bool,
                            sum_two,
                            join_str)


class Task1_Test(unittest.TestCase):

    def test_sum_two(self):
        self.assertEqual(sum_two(2, 1), 3)
        self.assertEqual(sum_two(-8, 6), -2)
        self.assertEqual(sum_two(-5, -5), -10)

    def test_sum_float(self):
        self.assertEqual(sum_float(4.0, 1.5), 5.5)
        self.assertEqual(sum_float(7.0, 6.0), 13.0)
        self.assertEqual(sum_float(2.894, 4.106), 7.0)

    def test_join_str(self):
        self.assertEqual(join_str("Hello", "World"), "HelloWorld")
        self.assertEqual(join_str("", "Hi"), "Hi")

    def test_invert_bool(self):
        self.assertFalse(invert_bool(True))
        self.assertTrue(invert_bool(False))

        # Check incorrect arguments
        self.assertRaises(TypeError, invert_bool, 1)
        self.assertRaises(TypeError, invert_bool, "True")
