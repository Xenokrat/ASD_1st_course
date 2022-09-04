import unittest
from deque import Deque
from deque_palindrome import is_palindrome


class TestDeque(unittest.TestCase):
    def test_deque(self):
        dq = Deque()
        self.assertEqual(dq.size(), 0)

        dq.addFront(0)
        dq.addFront(1)
        dq.addFront(2)
        dq.addFront(3)
        self.assertListEqual(dq.array, [3, 2, 1, 0])
        self.assertEqual(dq.size(), 4)

        dq.addTail(1)
        dq.addTail(2)
        dq.addTail(3)
        self.assertListEqual(dq.array, [3, 2, 1, 0, 1, 2, 3])
        self.assertEqual(dq.size(), 7)

        dq.removeFront()
        dq.removeFront()
        self.assertListEqual(dq.array, [1, 0, 1, 2, 3])
        self.assertEqual(dq.size(), 5)

        dq.removeTail()
        dq.removeTail()
        self.assertListEqual(dq.array, [1, 0, 1])
        self.assertEqual(dq.size(), 3)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome('Eva, can I see bees in a cave?'))
        self.assertTrue(is_palindrome('Step on no pets.'))

        self.assertFalse(is_palindrome('text'))
        self.assertFalse(is_palindrome('word'))
        self.assertFalse(is_palindrome('Some sentence, I dunno.'))


if __name__ == '__main__':
    unittest.main()
