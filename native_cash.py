class NativeCache:
    def __init__(self, sz: int) -> None:
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        
    def hash_func(self, key: str) -> int:
        """Return index to insert in array

        Args:
            key (str): text to hash

        Returns:
            int: index
        """
        res = 0
        for char in key:
            res = (res + ord(char)) % self.size
        return res

    def put(self, key: str, value: str) -> int:
        """Put key/value pair in arrays, 
           delete least used key if nessesary

        Args:
            key (str): key text
            value (str): value text

        Returns:
            int: index where key/value inserted
        """
        pos = self.hash_func(key)
        counter = 0

        while counter < self.size:
            slot = self.slots[pos]
            if (slot is None) or (slot == key):
                self.slots[pos] = key
                self.values[pos] = value
                return pos

            pos = (pos + 3) % self.size
            counter += 1
        
        # call delete least used key if cannot put
        pos = self.delete_least_used()
        self.slots[pos] = key
        self.values[pos] = value
        
    def is_key(self, key: str) -> bool:
        """Check if key in array

        Args:
            key (str): key text to search

        Returns:
            bool: True if key exists, else False
        """
        pos = self.hash_func(key)
        counter = 0
        
        while counter < self.size:
            slot = self.slots[pos]
            if slot == key:
                return True

            pos = (pos + 3) % self.size
            counter += 1

        return False
        
    def get(self, key: str) -> str:
        """Get value by key

        Args:
            key (str): key to get value

        Returns:
            str: value text
        """
        pos = self.hash_func(key)
        counter = 0
        
        while counter < self.size:
            slot = self.slots[pos]
            if slot == key:
                self.hits[pos] += 1
                return self.values[pos]

            pos = (pos + 3) % self.size
            counter += 1
            
    def delete_least_used(self) -> int:
        """Delete least used key 

        Returns:
            int: return deleted index
        """
        min_hits = min(self.hits)
        min_hits_index = self.hits.index(min_hits)

        self.slots[min_hits_index] = None
        self.values[min_hits_index] = None
        self.hits[min_hits_index] = 0

        return min_hits_index
        