import unittest

from ordered_list import OrderedList, OrderedStringList

def make_test_list() -> OrderedList:
    o_list = OrderedList(asc=True)
    for i in (1, 3, 8, 7, 2):
        o_list.add(i)
    return o_list

def make_test_list_rev() -> OrderedList:
    o_list = OrderedList(asc=False)
    for i in (1, 3, 8, 7, 2):
        o_list.add(i)
    return o_list

def make_test_list_str() -> OrderedStringList:
    o_list = OrderedStringList(asc=True)
    for i in ('a', 'b ', ' z', 'm', 'y'):
        o_list.add(i)
    return o_list

def make_test_list_str_rev() -> OrderedStringList:
    o_list = OrderedStringList(asc=False)
    for i in ('a', 'b ', ' z', 'm', 'y'):
        o_list.add(i)
    return o_list

class TestOrderedList(unittest.TestCase):
    def test_is_ordered(self) -> None:
        o_list = make_test_list()
        self.assertEqual(o_list.head.value, 1)
        self.assertEqual(o_list.tail.value, 8)
        
        self.assertEqual(o_list.head.next.value, 2)
        self.assertEqual(o_list.head.next.next.value, 3)
        self.assertEqual(o_list.tail.prev.value, 7)
        self.assertEqual(o_list.tail.prev.prev.value, 3)

    def test_is_ordered_rev(self) -> None:
        o_list = make_test_list_rev()
        self.assertEqual(o_list.head.value, 8)
        self.assertEqual(o_list.tail.value, 1)
        
        self.assertEqual(o_list.head.next.value, 7)
        self.assertEqual(o_list.head.next.next.value, 3)

        self.assertEqual(o_list.tail.prev.value, 2)
        self.assertEqual(o_list.tail.prev.prev.value, 3)


    def test_find(self) -> None:
        o_list = make_test_list()

        for i in (1, 3, 8, 7, 2):
            self.assertEqual(o_list.find(i).value, i)

        for i in (0, 4, 5, 6):
           self.assertIsNone(o_list.find(i))

    def test_find_rev(self) -> None:
        o_list = make_test_list_rev()

        for i in (1, 3, 8, 7, 2):
            self.assertEqual(o_list.find(i).value, i)

        for i in (0, 4, 5, 6):
           self.assertIsNone(o_list.find(i))

    def test_delete(self) -> None:
        o_list = make_test_list()
        len_ = 5

        for i in (1, 3, 8, 7, 2):
            o_list.delete(i)
            len_ -= 1
            self.assertEqual(o_list.len(), len_)

        self.assertIsNone(o_list.head)
        self.assertIsNone(o_list.tail)

    def test_delete_rev(self) -> None:
        o_list = make_test_list_rev()
        len_ = 5

        for i in (1, 3, 8, 7, 2):
            o_list.delete(i)
            len_ -= 1
            self.assertEqual(o_list.len(), len_)

        self.assertIsNone(o_list.head)
        self.assertIsNone(o_list.tail)


    def test_is_ordered_str(self) -> None:
        o_list = make_test_list_str()
        self.assertEqual(o_list.head.value, 'a')
        self.assertEqual(o_list.tail.value, ' z')
        
        self.assertEqual(o_list.head.next.value, 'b ')
        self.assertEqual(o_list.head.next.next.value, 'm')
        self.assertEqual(o_list.tail.prev.value, 'y')
        self.assertEqual(o_list.tail.prev.prev.value, 'm')

    def test_is_ordered_str_rev(self) -> None:
        o_list = make_test_list_str_rev()
        self.assertEqual(o_list.head.value, ' z')
        self.assertEqual(o_list.tail.value, 'a')
        
        self.assertEqual(o_list.head.next.value, 'y')
        self.assertEqual(o_list.head.next.next.value, 'm')
        self.assertEqual(o_list.tail.prev.value, 'b ')
        self.assertEqual(o_list.tail.prev.prev.value, 'm')

    def test_find_str(self) -> None:
        o_list = make_test_list_str()

        for i in ('a', 'b ', ' z', 'm', 'y'):
            self.assertIsNotNone(o_list.find(i))

        for i in ('c', 'd', 'q', 't'):
           self.assertIsNone(o_list.find(i))

    def test_delete_str(self) -> None:
        o_list = make_test_list_str()
        len_ = 5

        for i in ('a', 'b ', ' z', 'm', 'y'):
            o_list.delete(i)
            len_ -= 1
            self.assertEqual(o_list.len(), len_)

        self.assertIsNone(o_list.head)
        self.assertIsNone(o_list.tail)


if __name__ == '__main__':
    unittest.main()