import unittest
import random

from native_dictionary import NativeDictionary


def create_hash_table(sz: int) -> NativeDictionary:
    return NativeDictionary(sz)

def create_rand_data(len_: int) -> list[str]:
    rand_data = random.sample(range(30), len_)
    res = ['1' * num for num in rand_data]
    return res

class TestNativeDict(unittest.TestCase):
    def test_is_key(self) -> None:
        table = create_hash_table(19)
        rand_data = create_rand_data(19)
        for i, _ in enumerate(table.slots):
            table.slots[i] = rand_data[i]
            
        for key in rand_data:
            self.assertTrue(table.is_key(key))
        
        for key in ('kek', 'kok', 'hah', '0000000000000000'):
            self.assertFalse(table.is_key(key))
            
    def test_put(self) -> None:
        table = create_hash_table(7)
        rand_data = create_rand_data(7)
        test_data = (
            (rand_data[0], 'пластмассовый'),
            (rand_data[1], 'мир'),
            (rand_data[2], 'победил'),
            (rand_data[3], 'макет'),
            (rand_data[4], 'оказался'),
            (rand_data[5], 'сильней'),
            (rand_data[6], 'лал'),
        )
        
        # put test_data in table
        for i in test_data:
            table.put(i[0], i[1])
        
        # assert all key saved in native dict
        for i in test_data:
            self.assertTrue(i[0] in table.slots)

        # assert all values saved in native dict
        for i in test_data:
            self.assertTrue(i[1] in table.values)

    def test_get(self) -> None:
        table = create_hash_table(7)
        rand_data = create_rand_data(7)
        test_data = (
            (rand_data[0], 'пластмассовый'),
            (rand_data[1], 'мир'),
            (rand_data[2], 'победил'),
            (rand_data[3], 'макет'),
            (rand_data[4], 'оказался'),
            (rand_data[5], 'сильней'),
            (rand_data[6], 'лал'),
        )
        
        for i in test_data:
            table.put(i[0], i[1])
            
        for i in test_data:
            self.assertEqual(table.get(i[0]), i[1])
