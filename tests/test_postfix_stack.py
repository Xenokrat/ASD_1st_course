import unittest
from postfix_stack import eval_postfix_expression


class TestPostfix(unittest.TestCase):
    def test_postfix(self):
        res1 = eval_postfix_expression('1 2 + 3 * =')
        res2 = eval_postfix_expression('8 2 + 5 * 9 + =')
        res3 = eval_postfix_expression('11 3 * 5 + 2 * =')
        self.assertEqual(res1, 9)
        self.assertEqual(res2, 59)
        self.assertEqual(res3, 76)


if __name__ == '__main__':
    unittest.main()
