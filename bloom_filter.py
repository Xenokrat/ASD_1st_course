class BloomFilter:
    def __init__(self, f_len: int) -> None:
        self.filter_len = f_len
        self.bitarray = 1 << f_len
        
    def hash1(self, str1: str) -> int:
        """Return position in bit array from 0 to filter_len
           use random number = 17

        Args:
            str1 (str): text to add

        Returns:
            int: position in bit array from 0 to filter_len
        """
        rand_num = 17
        res = 0
        for c in str1:
            code = ord(c)
            res = ((res * rand_num) + code) % self.filter_len
        return res
            
    def hash2(self, str2: str) -> int:
        """Return position in bit array from 0 to filter_len
           use random number = 223

        Args:
            str1 (str): text to add

        Returns:
            int: position in bit array from 0 to filter_len
        """
        rand_num = 223
        res = 0
        for c in str2:
            code = ord(c)
            res = ((res * rand_num) + code) % self.filter_len
        return res
        
    def add(self, str1: str) -> None:
        """Update bitarray - set 1 to results of hash funtions

        Args:
            str1 (str): text to add
        """
        pos1 = self.hash1(str1)
        pos2 = self.hash2(str1)
        self.bitarray = self.bitarray | 1 << pos1
        self.bitarray = self.bitarray | 1 << pos2
    
    def is_value(self, str1: str) -> bool:
        """Check if text in filter

        Args:
            str1 (str): text to add

        Returns:
            bool: False if text not in filter, 
                  True if text in filter,
                  may return True if text not in filter
        """
        pos1 = self.hash1(str1)
        pos2 = self.hash2(str1)
        return all([
            self.bitarray & 1 << pos1,  # if 0 then return False
            self.bitarray & 1 << pos2
        ])
    