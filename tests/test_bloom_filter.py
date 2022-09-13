import unittest
from typing import NoReturn

from bloom_filter import BloomFilter

class TestBloomFilter(unittest.TestCase):
    def test_add_check(self) -> NoReturn:
        x = BloomFilter(32)
        texts = (
            '0123456789', 
            '1234567890',
            '2345678901',
            '3456789012',
            '4567890123',
            '5678901234',
            '6789012345',
            '7890123456',
            '8901234567',
            '9012345678',
        )
        for text in texts:
            x.add(text)
            
        for text in texts:
            self.assertTrue(x.is_value(text))

        wrong_text = (
            '1111111111',
            '1111122222',
        )
        for text in wrong_text:
            self.assertFalse(x.is_value(text))
        