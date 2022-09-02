import unittest
from queue import Queue
from queue_rotate import rotate_queue


class TestQueue(unittest.TestCase):
    def test_queue(self):
        qu = Queue()
        self.assertEqual(qu.size(), 0)
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        self.assertEqual(qu.size(), 3)
        pop1 = qu.dequeue()
        self.assertEqual(pop1, 1)
        pop2 = qu.dequeue()
        self.assertEqual(pop2, 2)
        qu.dequeue()
        qu.dequeue()
        self.assertEqual(qu.size(), 0)

    def test_rotate_queue(self):
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        qu.enqueue(4)
        rotate_queue(qu, 3)
        self.assertEqual(qu.dequeue(), 4)
        rotate_queue(qu, 8)
        self.assertEqual(qu.dequeue(), 3)


if __name__ == '__main__':
    unittest.main()
