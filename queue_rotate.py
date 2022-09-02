from queue import Queue


def rotate_queue(qu: Queue, n: int) -> Queue:
    """
    :param qu: Queue object
    :param n: number of shifts
    :return: rotated Queue
    """

    for _ in range(n):
        temp = qu.dequeue()
        qu.enqueue(temp)
