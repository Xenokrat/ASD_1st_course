import unittest
import random

from native_cash import NativeCache

class TestNativeCash(unittest.TestCase):
    def test_smth(self) -> None:
        x = NativeCache(7)

        info_text = (
            ('The', '1'),
            ('best', '1'),
            ('climbers', '1'),
            ('know', '1'),
            ('how', '1'),
            ('to', '1'),
            ('fall', '1'),
        )
        
        for i in info_text:
            x.put(i[0], i[1])
            
        sample_info = [random.choice(info_text)[0] for _ in range(15)]

        for i in sample_info:
            x.get(i)
        
        min_hits = min(x.hits)
        min_hits_index = x.hits.index(min_hits)
        deleted_key = x.slots[min_hits_index]
        
        x.put('AAAAAAA', '1')
        
        self.assertTrue(x.is_key('AAAAAAA'))
        self.assertFalse(x.is_key(deleted_key))