import unittest
from dynamic_array import *


class TestDynArr(unittest.TestCase):
    def test_insert(self):
        # insert when buffer size not excesses
        x = DynArray()
        buff1 = x.capacity
        for i in range(15):
            x.append(i)
        x.insert(5, 50)
        self.assertEqual(x[5], 50)
        self.assertEqual(x.capacity, buff1)

        # insert when buffer size not excesses
        x.insert(10, 100)
        self.assertEqual(x[10], 100)
        self.assertEqual(x.capacity, 2 * buff1)

        # not allowed position
        self.assertRaises(IndexError, x.insert, 20, 200)

        # insert to array tail
        x.insert(17, 17)
        self.assertEqual(x[17], 17)

    def test_delete(self):
        # delete when buffer size not excesses
        x = DynArray()
        for i in range(50):
            x.append(i)
        buff1 = x.capacity  # 64
        x.delete(48)
        self.assertEqual(x[48], 49)
        self.assertEqual(x.capacity, buff1)

        # delete when buffer size not excesses
        for i in range(17):
            x.delete(0)
            self.assertEqual(x.capacity, buff1)
        x.delete(0)
        self.assertEqual(x.capacity, int(buff1 / 1.5))

        # not allowed position
        self.assertRaises(IndexError, x.delete, 100)


if __name__ == '__main__':
    unittest.main()
