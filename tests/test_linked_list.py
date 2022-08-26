import unittest
from linked_list import *


def construct_many_elements_list():
    s_list = LinkedList()
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
    return s_list


def construct_one_element_list():
    s_list = LinkedList()
    s_list.add_in_tail(Node(1))
    return s_list


def construct_empty_list():
    return LinkedList()


class MyTestCase(unittest.TestCase):

    def test_delete(self):
        empty_list = construct_empty_list()
        empty_list.delete(1)
        self.assertEqual(empty_list.head, None)
        self.assertEqual(empty_list.tail, None)

        one_list = construct_one_element_list()
        one_list.delete(1)
        self.assertEqual(one_list.head, None)
        self.assertEqual(one_list.tail, None)

        one_list = construct_one_element_list()
        one_list.delete(1, all=True)
        self.assertEqual(one_list.head, None)
        self.assertEqual(one_list.tail, None)

        # [1, 2, 2, 4, 8, 1]
        many_list = construct_many_elements_list()
        many_list.delete(8)
        self.assertEqual(many_list.find(8), None)

        many_list = construct_many_elements_list()
        many_list.delete(1)
        self.assertEqual(many_list.find(1), many_list.tail)
        self.assertEqual(many_list.head.value, 2)

        many_list = construct_many_elements_list()
        many_list.delete(1, all=True)
        self.assertEqual(many_list.head.value, 2)
        self.assertEqual(many_list.tail.value, 8)

    def test_clean(self):
        one_list = construct_one_element_list()
        many_list = construct_many_elements_list()
        one_list.clean()
        many_list.clean()
        self.assertEqual(one_list.head, None)
        self.assertEqual(many_list.head, None)
        self.assertEqual(one_list.tail, None)
        self.assertEqual(many_list.tail, None)

    def test_find_all(self):
        s_list = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)
        n4 = Node(4)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        res = s_list.find_all(2)
        self.assertListEqual(res, [n2, n3])

    def test_len(self):
        empty_list = construct_empty_list()
        one_list = construct_one_element_list()
        many_list = construct_many_elements_list()
        self.assertEqual(empty_list.len(), 0)
        self.assertEqual(one_list.len(), 1)
        self.assertEqual(many_list.len(), 6)

    def test_insert(self):
        s_list = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)
        n4 = Node(4)
        n5 = Node(5)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)

        s_list.insert(n1, n5)
        self.assertEqual(s_list.find(5), n5)

        s_list.insert(None, n5)
        self.assertEqual(s_list.head, n5)


if __name__ == '__main__':
    unittest.main()
