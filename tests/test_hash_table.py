import unittest

from hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def create_hash_table(self, sz: int, stp: int) -> HashTable:
        return HashTable(sz, stp)
    
    def test_hash_fun(self) -> None:
        table = self.create_hash_table(19, 3)
        res = table.hash_fun('kek kekov')
        self.assertEqual(res, 9)
        
        # assert it returns 0 
        res = table.hash_fun('aaaaaaaaaaaaaaaaaaa')
        self.assertEqual(res, 0)
        
        res = table.hash_fun('')
        self.assertEqual(res, 0)
    
    def test_seek_slot(self) -> None:
        table = self.create_hash_table(19, 3)
        
        # assert return index on empty slot
        res = table.seek_slot('kek kekov')  # == 9
        self.assertEqual(res, 9)
        
        # assert return index on non-empty slot through 1 step 
        table.slots[9] = 1
        res = table.seek_slot('kok kekov')  # == 9
        self.assertEqual(res, 12)
        
        # assert return index on non-empty slot through > 1 going from start
        table.slots[12] = 1
        table.slots[15] = 1
        table.slots[18] = 1
        res = table.seek_slot('kok kekov')  # == 9
        self.assertEqual(res, 2)
        
        # assert return None when when cannot find empty slot
        for ind, _ in enumerate(table.slots):
            table.slots[ind] = 1
        res = table.seek_slot('kok kekov')  # == 9
        self.assertIsNone(res)
    
    def test_put(self) -> None:
        table = self.create_hash_table(19, 3)
        
        # assert put in slot inplace, then put duplicate
        table.put('kek kekov')
        self.assertEqual(table.slots[9], 'kek kekov')
        res = table.put('kek kekov')
        self.assertEqual(table.slots[9], 'kek kekov')
        self.assertEqual(res, 9)
        
        table.put('aaaaaaaaaaaaaaaaaaaa')
        self.assertEqual(table.slots[1], 'aaaaaaaaaaaaaaaaaaaa')
        
        # assert right shift by step
        table.slots[18] = 1
        table.put('bbbbbbbbbbbbbbbbbb')
        self.assertEqual(table.slots[2], 'bbbbbbbbbbbbbbbbbb')
        table.put('cccccccccccccccccc')
        self.assertEqual(table.slots[5], 'cccccccccccccccccc')
        
        for ind, _ in enumerate(table.slots):
            table.slots[ind] = 1
        res = table.put('aaaaaaaaaaaaaaaaaaaa')
        self.assertIsNone(res)
        
        # assert correct insertion to index 0
        table = self.create_hash_table(19, 3)
        text = ''
        for _ in range(19):
            table.put(text)
            text += '1'
            
        text = ''
        for ind in range(19):
            self.assertEqual(table.slots[ind], text)
            text += '1'
        
    
    def test_find(self) -> None:
        table = self.create_hash_table(19, 3)
        table.slots[18] = 1
        table.put('kek kekov')
        table.put('aaaaaaaaaaaaaaaaaaaa')
        table.put('bbbbbbbbbbbbbbbbbb')
        table.put('cccccccccccccccccc')
        
        # assert we can find this in table
        self.assertEqual(table.find('kek kekov'), 9)
        self.assertEqual(table.find('aaaaaaaaaaaaaaaaaaaa'), 1)
        self.assertEqual(table.find('bbbbbbbbbbbbbbbbbb'), 2)
        self.assertEqual(table.find('cccccccccccccccccc'), 5)
        
        # assert we cannot find what is not in the table
        self.assertIsNone(table.find('mda'))
        self.assertIsNone(table.find('fuuuuuuuuuuuuuuuu'))
        
        # more tests
        table = self.create_hash_table(19, 3)
        text = ''
        for _ in range(19):
            table.put(text)
            text += '1'
            
        text = ''
        for _ in range(19):
            find_text = table.find(text)
            self.assertEqual(table.slots[find_text], text)
            text += '1'
            
        # more tests
        table = self.create_hash_table(19, 3)
        text = '11111111111'
        for _ in range(19):
            table.put(text)
            text += '1'
            
        text = '11111111111'
        for _ in range(19):
            find_text = table.find(text)
            self.assertEqual(table.slots[find_text], text)
            text += '1'
    
    
    def test_cycle_around(self) -> None:
        table = self.create_hash_table(19, 3)
        
        index = 0
        bool_flag = False
        index, bool_flag = table.cycle_around(index, bool_flag)
        self.assertEqual(index, 3)
        self.assertFalse(bool_flag)
        
        index = 17
        index, bool_flag = table.cycle_around(index, bool_flag)
        self.assertEqual(index, 1)
        self.assertTrue(bool_flag)
    
        