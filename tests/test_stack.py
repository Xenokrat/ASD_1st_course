import unittest
from stack import *
from stack_brackets import is_brackets_balanced


class TestStack(unittest.TestCase):
    def test_stack(self):
        x = Stack()
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

    def test_bracket_balanced(self):
        res1 = is_brackets_balanced('(()((())()))')
        res2 = is_brackets_balanced('()()()')
        res3 = is_brackets_balanced('(()((())()))')

        res4 = is_brackets_balanced('())(')
        res5 = is_brackets_balanced('))((')
        res6 = is_brackets_balanced('((())')

        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertTrue(res3)

        self.assertFalse(res4)
        self.assertFalse(res5)
        self.assertFalse(res6)


if __name__ == '__main__':
    unittest.main()
