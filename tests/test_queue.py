import unittest
from queue import Queue
from queue_rotate import rotate_queue
from queue_2_stacks import QueueStacked


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

    def test_queue_stacked(self):
        qus = QueueStacked()
        self.assertEqual(qus.size(), 0)
        qus.enqueue(1)
        qus.enqueue(2)
        qus.enqueue(3)
        self.assertEqual(qus.size(), 3)
        pop1 = qus.dequeue()
        self.assertEqual(pop1, 1)
        pop2 = qus.dequeue()
        self.assertEqual(pop2, 2)
        qus.dequeue()
        qus.dequeue()
        self.assertEqual(qus.size(), 0)


if __name__ == '__main__':
    unittest.main()
