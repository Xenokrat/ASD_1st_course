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
        
        bool_flag = False  # show if we cycle to end of array and iterate from start
        while not (index >= current_index and bool_flag):
            slot = self.slots[index]
            
            # ? what if we put same value twice?
            if (slot is None) or (slot == value):
                return index
            index, bool_flag = self.cycle_around(index, bool_flag)
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
        if index:
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
        current_index = index
        
        bool_flag = False  # show if we cycle to end of array and iterate from start
        while not (index >= current_index and bool_flag):
            slot = self.slots[index]
            
            if slot == value:
                return index
            index, bool_flag = self.cycle_around(index, bool_flag)
        return None
    
    def cycle_around(self, index: int, bool_flag: bool) -> tuple:
        """Returns index + step for array, starts from beginning of array
           if index out of boundaries

        Args:
            index (int): start position
            bool_flag (bool): True if started from beginning

        Returns:
            tuple: new index (index + step), do index started from beginning
        """
        size = self.size
        step = self.stp
        
        next_index = index + step
        if next_index > size - 1:
            bool_flag = True
            return next_index - size, bool_flag
        return next_index, bool_flag
            
            