import unittest
import random
import time

from power_set import PowerSet

class TestPowerSet(unittest.TestCase):
    def test_put(self) -> None:
        # add element, 
        # cannot add element that already in set
        x = PowerSet()
        words = ('some', 'random', 'random', 'sh*t', 'to', 'to', 'add')
        for text in words:
            x.put(text)
        
        for text in words:
            self.assertTrue(text in x.container)
        
        self.assertEqual(x.size(), 5)
    
    def test_remove(self) -> None:
        x = PowerSet()
        words = ('some', 'random', 'random', 'sh*t', 'to', 'to', 'add')
        for text in words:
            x.put(text)
            
        # normal deletion for items in container
        remove_list = ('some', 'to', 'add')
        for text in remove_list:    
            self.assertTrue(x.remove(text))
            self.assertFalse(text in x.container)
            
        # it's ok to try delete item not in container
        self.assertFalse(x.remove('kek'))
    
    def test_intersection(self) -> None:
        # can return empty set if no intersection 
        # and non-empty
        x = PowerSet()
        y = PowerSet()

        words1 = ('some', 'random', 'sh*t', 'to', 'add')
        words2 = ('some', 'random', 'but', 'not', 'same', 'sh*t')
        
        for i in words1:
            x.put(i)

        for i in words2:
            y.put(i)
        
        z = x.intersection(y)
        words_check = ('some', 'random', 'sh*t')
        for word in words_check:
            self.assertTrue(z.get(word))
            
        x = PowerSet()
        y = PowerSet()

        words1 = ('this', 'words', 'do', 'not', 'match')
        words2 = ('where', 'is', 'my', 'pepper')
        
        for i in words1:
            x.put(i)

        for i in words2:
            y.put(i)
        
        z = x.intersection(y)
        self.assertEqual(z.size(), 0)
    
    def test_union(self) -> None:
        # both non-empty
        x = PowerSet()
        y = PowerSet()

        words1 = ('some', 'random', 'sh*t', 'to', 'add')
        words2 = ('some', 'random', 'but', 'not', 'same', 'sh*t')
        
        for i in words1:
            x.put(i)

        for i in words2:
            y.put(i)
        
        z = x.union(y)
        for i in ('some', 'random', 'sh*t', 'to', 'add', 'but', 'not', 'same'):
            self.assertTrue(i in z.container)

        # one empty
        y = PowerSet()
        z = x.union(y)

        for i in ('some', 'random', 'sh*t', 'to', 'add'):
            self.assertTrue(i in z.container)
        
        # both empty
        x = PowerSet()
        z = x.union(y)
        self.assertEqual(z.size(), 0)
    
    def test_difference(self) -> None:
        x = PowerSet()
        y = PowerSet()

        words1 = ('some', 'random', 'sh*t', 'to', 'add')
        words2 = ('some', 'random', 'but', 'not', 'same', 'sh*t')
        
        for i in words1:
            x.put(i)

        for i in words2:
            y.put(i)
        
        z = x.difference(y)
        self.assertEqual(z.size(), 2)
        for i in ('to', 'add'):
            self.assertTrue(i in z.container)
            
        x = PowerSet()
        y = PowerSet()

        words1 = ('this', 'words', 'do', 'not', 'match')
        words2 = ('where', 'is', 'my', 'pepper')
        
        z = x.difference(y)
        self.assertEqual(z.size(), 0)
    
    def test_issubset(self) -> None:
        x = PowerSet()
        y = PowerSet()

        words1 = ('word1', 'word2', 'word3', 'word4', 'word5')
        words2 = ('word1', 'word3', 'word5')
        
        for i in words1:
            x.put(i)

        for i in words2:
            y.put(i)
            
        # set @> subset
        self.assertTrue(x.issubset(y))
        # set <@ sub-set
        self.assertFalse(y.issubset(x))
        
        # subset have non-common elements with subset
        y.put('outer word')
        self.assertFalse(x.issubset(y))
    
    def test_speed(self) -> None:
        rand_data = (random.randint(1, 20000) for _ in range(20000))
        x = PowerSet()
        y = PowerSet()

        for num in rand_data:
            x.put(num)

        for num in rand_data:
            y.put(num)
            
        start_time = time.time()
        z = x.intersection(y)
        self.assertLess(time.time() - start_time, 1)

        start_time = time.time()
        z = x.difference(y)
        self.assertLess(time.time() - start_time, 1)

        start_time = time.time()
        z = x.union(y)
        self.assertLess(time.time() - start_time, 1)

        start_time = time.time()
        z = x.issubset(y)
        self.assertLess(time.time() - start_time, 1)
        