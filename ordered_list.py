class Node:
    def __init__(self, v) -> None:
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc: bool) -> None:
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1: int, v2: int) -> int:
        if v1 < v2:
            res = -1
        elif v1 > v2:
            res = 1
        else:
            res = 0
        
        if not self.__ascending:
            res = res * -1
        
        return res

    def add(self, node_value) -> None:
        node_to_write = Node(node_value)

        # add to empty list
        if self.head is None:
            self.tail = node_to_write
            self.head = node_to_write
            return None

        if self.compare(node_value, self.head.value) == -1:
            node_to_write.next = self.head
            self.head.prev = node_to_write
            self.head = node_to_write
            return None

        if self.compare(node_value, self.tail.value) in (0, 1):
            node_to_write.prev = self.tail
            self.tail.next = node_to_write
            self.tail = node_to_write
            return None

        node = self.head
        while node is not None:
            compare_next = self.compare(
                node.next.value,
                node_to_write.value,
            )

            if compare_next in (0, 1):
                node_to_write.next = node.next
                node_to_write.prev = node
                node.next.prev = node_to_write
                node.next = node_to_write
                return None

            node = node.next

    def find(self, val: int):
        
        # list is empty
        if self.head is None:
            return None
        
        if any([
            self.compare(val, self.head.value) == -1,  # value less than head
            self.compare(val, self.tail.value) == 1    # value bigger than tail
        ]):
            return None

        node = self.head
        while node is not None:
            if self.compare(val, node.value) == 0:
                return node
            elif self.compare(val, node.value) == -1:
                return None  # stop as value not in list
            node = node.next

        return None

    def delete(self, val) -> None:

        # empty list
        if self.head is None:
            return None

        # one element list
        if self.head == self.tail and self.head.value == val:
            self.head = None
            self.tail = None
            return None

        # if it's head
        elif self.head.value == val:
            self.head = self.head.next
            self.head.prev = None
            return None

        # if it's tail
        elif self.tail.value == val:
            self.tail = self.tail.prev
            self.tail.next = None
            return None

        node = self.head
        while node is not None:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                return None
            
            # break by order-check
            if self.compare(val, node.value) == -1:
                return None

            node = node.next

    def clean(self, asc: bool) -> None:
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self) -> int:
        node = self.head
        counter = 0
        while node is not None:
            counter += 1
            node = node.next

        return counter

    def get_all(self):
        result = []
        node = self.head
        while node is not None:
            result.append(node)
            node = node.next
        return result


class OrderedStringList(OrderedList):
    def __init__(self, asc: bool) -> None:
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str) -> int:
        v1, v2 = v1.strip(), v2.strip()
        if v1 < v2:
            res = -1
        elif v1 > v2:
            res = 1
        else:
            res = 0
        
        if not self._OrderedList__ascending:
            res = res * -1
        
        return res
