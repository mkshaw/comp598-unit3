import unittest

from ..fib import generate_fib_sequence

class FibTestCase(unittest.TestCase):
    
    def test_generate3(self):

        values = generate_fib_sequence(3)

        self.assertEqual(values, [1, 1, 2])

    def test_generate10(self):

        values = generate_fib_sequence(10)

        self.assertEqual(len(values), 10)

    def test_generate1(self):

        with self.assertRaises(Exception) as context:
            generate_fib_sequence(1)

        self.assertTrue(context.exception)
