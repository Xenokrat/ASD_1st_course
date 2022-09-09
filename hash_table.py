class HashTable:
    def __init__(self, sz: int, stp: int) -> None:
        self.size = sz
        self.stp = stp
        self.slots = [None] * self.size
        
    def hash_fun(self, value: str) -> int:
        """Calculate slot index based on value

        Args:
            value (str): string value for hashing

        Returns:
            int: slot index
        """
        byte_len = len(value.encode('utf-8'))
        hash_ = byte_len % self.size
        return hash_

    def seek_slot(self, value: str) -> int:
        """Find slot for insertion considering collisions

        Args:
            value (str): string value for insertion

        Returns:
            int: index of array for insertion considering collisions 
            or None if not possible
        """
        index = self.hash_fun(value)
        current_index = index
        
        counter = 0
        while counter < self.size:
            slot = self.slots[index]
            
            if (slot is None) or (slot == value):
                return index
            index = (index + self.stp) % self.size
            counter += 1
            
        return None
            
    def put(self, value: str) -> int:
        """put value in slot if possible and return index, else return None

        Args:
            value (str): string value for insertion

        Returns:
            int: index of array for insertion considering collisions 
            or None if not possible
        """
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        return index

    def find(self, value: str) -> int:
        """find value index in hash-table

        Args:
            value (str): value to find

        Returns:
            int: index of value in array or None
        """
        index = self.hash_fun(value)
        
        counter = 0
        while counter < self.size:
            slot = self.slots[index]
            
            if slot == value:
                return index
            index = (index + self.stp) % self.size
            counter += 1
        return None
    