import unittest
from number import *


class TestNumbers(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(15485863))
        self.assertTrue(is_prime(838041647))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(63))
        self.assertFalse(is_prime(2046))
        self.assertFalse(is_prime(123))

    def test_lpf(self):
        self.assertEqual(29, largest_prime_factor(13195))


if __name__ == '__main__':
    unittest.main()
