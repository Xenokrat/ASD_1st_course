import unittest
from stack_reverse import *


class TestStack(unittest.TestCase):
    def test_stack(self):
        x = StackReverse()
        x.push(0)
        x.push(1)
        x.push(2)
        self.assertEqual(x.peek(), 2)
        self.assertEqual(x.size(), 3)

        x.pop()
        x.pop()
        self.assertEqual(x.peek(), 0)
        self.assertEqual(x.size(), 1)
        x.pop()
        y = x.pop()
        self.assertIsNone(y)
        self.assertEqual(x.size(), 0)


if __name__ == '__main__':
    unittest.main()
