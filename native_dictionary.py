class NativeDictionary:
    def __init__(self, sz: int) -> None:
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
    
    def hash_fun(self, key: str) -> int:
        """Calculate slot index based on key

        Args:
            key (str): string value for hashing

        Returns:
            int: slot index 
        """
        byte_len = len(key.encode('utf-8'))
        index = byte_len % self.size
        return index

    
    def is_key(self, key: str) -> bool:
        """Check if key exists

        Args:
            key (str): string value for hashing

        Returns:
            bool: True if key exists, else False
        """
        index = self.hash_fun(key)
        counter = 0

        while counter < self.size:
            slot = self.slots[index]
            if slot == key:
                return True
            index = (index + 3) % self.size
            counter += 1

        return False
    
    def put(self, key: str, value: str) -> int:
        pass
    
    def get(self, key: str) -> str:
        pass

    