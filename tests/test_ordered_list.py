import unittest

from ordered_list import OrderedList, OrderedStringList


class TestOrderedList(unittest.TestCase):
    def test_ordered_list(self):
        o_list = OrderedList(asc=True)
        o_list.add(1)
        o_list.add(3)
        o_list.add(2)
        o_list.add(8)
