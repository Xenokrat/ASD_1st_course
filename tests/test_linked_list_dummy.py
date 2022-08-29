import unittest
from linked_list_dummy import *


class TestLinkedListDummy(unittest.TestCase):
    def test_find(self):
        s_list = LinkedListDummy()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)
        n4 = Node(4)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        res1 = s_list.find(1)
        res2 = s_list.find(2)
        res3 = s_list.find(4)
        self.assertEqual(res1, n1)
        self.assertEqual(res2, n2)
        self.assertEqual(res3, n4)

    def test_find_all(self):
        s_list = LinkedListDummy()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)
        n4 = Node(4)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        res1 = s_list.find_all(4)
        res2 = s_list.find_all(2)
        self.assertListEqual(res1, [n4])
        self.assertListEqual(res2, [n2, n3])

    def test_delete(self):
        s_list = LinkedListDummy()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)
        n4 = Node(4)
        n5 = Node(8)
        n6 = Node(1)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)
        s_list.add_in_tail(n6)

        s_list.delete(8)
        self.assertEqual(s_list.find(8), None)
        self.assertEqual(s_list.head, n1)
        self.assertEqual(s_list.tail, n6)

        s_list.delete(1)
        self.assertEqual(s_list.find(1), n6)
        self.assertEqual(s_list.head, n2)
        self.assertEqual(s_list.tail, n6)

        s_list.delete(2, all=True)
        self.assertEqual(s_list.find(2), None)
        self.assertEqual(s_list.head, n4)
        self.assertEqual(s_list.tail, n6)

        s_list.delete(1)
        s_list.delete(4)
        self.assertEqual(s_list.head, s_list.tail)
        self.assertEqual(s_list.tail, s_list.head)

        s_list.delete(10)
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

    def test_clean(self):
        s_list = LinkedListDummy()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        self.assertIsNotNone(s_list.head)
        self.assertIsNotNone(s_list.tail)

        s_list.clean()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_len(self):
        s_list = LinkedListDummy()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)

        self.assertEqual(s_list.len(), 3)

        s_list.delete(2, all=True)
        self.assertEqual(s_list.len(), 1)

        s_list.clean()
        self.assertEqual(s_list.len(), 0)

    def test_insert(self):
        s_list = LinkedListDummy()
        n1 = Node(1)

        s_list.insert(None, n1)
        self.assertEqual(s_list.head, n1)
        self.assertEqual(s_list.tail, n1)

        n2 = Node(2)
        s_list.insert(None, n2)
        self.assertEqual(s_list.head, n1)
        self.assertEqual(s_list.tail, n2)

        n3 = Node(3)
        s_list.insert(n1, n3)
        self.assertEqual(s_list.head, n1)
        self.assertEqual(s_list.tail, n2)
        self.assertEqual(s_list.head.next, n3)

    def test_add_id_head(self):
        s_list = LinkedListDummy()

        n1 = Node(1)
        s_list.add_in_head(n1)
        self.assertEqual(s_list.head, n1)
        self.assertEqual(s_list.tail, n1)

        n2 = Node(2)
        s_list.add_in_head(n2)
        self.assertEqual(s_list.head, n2)
        self.assertEqual(s_list.tail, n1)


if __name__ == '__main__':
    unittest.main()
