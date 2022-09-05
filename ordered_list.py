class Node:
    def __init__(self, v: (int | str)) -> None:
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
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0

    def add(self, value):
        node_to_write = Node(value)

        # write to empty list
        if self.head is None:
            self.tail = node_to_write
            self.head = node_to_write
            return None

        if self.compare(value, self.head.value) == -1:
            self.head.prev = node_to_write
            node_to_write.next = self.head
            self.head = node_to_write
            return None

        if self.compare(value, self.tail.value) in (0, 1):
            self.tail.next = node_to_write
            node_to_write.prev = self.tail
            self.tail = node_to_write
            return None

        current_node = self.head
        while current_node is not None:
            compare_here = self.compare(
                current_node.value,
                node_to_write.value,
            )

            compare_next = self.compare(
                current_node.next.value,
                node_to_write.value,
            )

            if compare_here in (-1, 0) and compare_next == 1:
                node_to_write.prev = current_node
                node_to_write.next = current_node.next
                current_node.next = node_to_write
                current_node.next.prev = node_to_write
                return None

    def find(self, val):
        return None  # здесь будет ваш код

    def delete(self, val):
        node = self.head
        first_deleted = False
        while node is not None:

            # break if we already deleted first value
            if first_deleted and not all:
                return None

            if ((node.value == val)
                    and (node == self.head)
                    and (node == self.tail)):
                self.head = None
                self.tail = None

            # if it's head
            elif (node.value == val) and (node == self.head):
                self.head = node.next
                self.head.prev = None
                first_deleted = True

            # if it's tail
            elif (node.value == val) and (node == self.tail):
                self.tail = node.prev
                self.tail.next = None
                first_deleted = True

            elif node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                first_deleted = True

            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        return 0  # здесь будет ваш код

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

    def compare(self, v1: str, v2: str) -> bool:
        v1, v2 = v1.strip(), v2.strip()

        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1
        return 0
