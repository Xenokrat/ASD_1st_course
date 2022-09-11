class PowerSet:
    def __init__(self) -> None:
        self.container = {}

    def size(self) -> int:
        """
        Returns:
            int: length of set
        """
        return len(self.container)

    def put(self, value) -> None:
        """Add any value in set, set have no duplicates

        Args:
            value (_type_): value to add
        """
        self.container[value] = None

    def get(self, value) -> bool:
        """Returns True if value in set, False if not

        Args:
            value (_type_): value to check in set

        Returns:
            bool: True if value in set, False if not
        """
        return (value in self.container)

    def remove(self, value) -> bool:
        """Delete value in set, return True if succeed, False if value
           not in set

        Args:
            value (_type_): value to delete

        Returns:
            bool: True if value deleted, else False
        """
        if self.get(value):
            del self.container[value]
            return True
        return False

    def intersection(self, set2):
        """Return intersection of current set and another set

        Args:
            set2 (PowerSet): another instance of PowerSet

        Returns:
            PowerSet: set of elements that is intersection 
            of current set and another set
        """
        new_set = PowerSet()
        
        for item in self.container:
            if set2.get(item):
                new_set.put(item)
                
        return new_set

    def union(self, set2):
        """Return union of elements between current set and another set

        Args:
            set2 (PowerSet): another instance of PowerSet

        Returns:
            PowerSet: PowerSet that is union of elements of current set
            and another set
        """
        new_set = PowerSet()
        for item in self.container:
            new_set.put(item)
        for item in set2.container:
            new_set.put(item)
        return new_set

    def difference(self, set2):
        """Return elements that is in current set but not in another set

        Args:
            set2 (PowerSet): set to compare

        Returns:
            PowerSet: difference between current set and another set
        """
        new_set = PowerSet()
        
        for item in self.container:
            if not set2.get(item):
                new_set.put(item)
                
        return new_set

    def issubset(self, set2) -> bool:
        """Return True if set2 is a subset of current set, else return False

        Args:
            set2 (PowerSet): another instance of PowerSet
            
        Returns:
            bool: True if set2 is a subset of current set, else return False
        """
        return all(
            item in self.container 
            for item in set2.container
        )