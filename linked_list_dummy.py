class Node:
    def __init__(self, v):
        self.prev = None
        self.next = None
        self.value = v


class LinkedListDummy:
    def __init__(self):
        self.__head = Node(None)
        self.__tail = Node(None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    @property
    def head(self):
        if self.__head.next == self.__tail:
            return None
        else:
            return self.__head.next

    @property
    def tail(self):
        if self.__tail.prev == self.__head:
            return None
        else:
            return self.__tail.prev

    def add_in_tail(self, item):
        item.next = self.__tail
        item.prev = self.__tail.prev
        self.__tail.prev.next = item
        self.__tail.prev = item

    def add_in_head(self, item):
        item.next = self.__head.next
        item.prev = self.__head
        self.__head.next.prev = item
        self.__head.next = item

    def find(self, val):
        node = self.__head.next
        while node != self.__tail:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.__head.next
        res = []
        while node != self.__tail:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def print_all_nodes(self):
        node = self.__head.next
        while node != self.__tail:
            print(node.value)
            node = node.next

    def delete(self, val, all=False):
        node = self.__head.next
        first_deleted = False
        while node != self.__tail:
            if first_deleted and not all:
                return None

            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                first_deleted = True

            node = node.next

        return None

    def clean(self):
        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    def len(self):
        counter = 0
        node = self.__head.next
        while node is not self.__tail:
            counter += 1
            node = node.next
        return counter

    def insert(self, after_node, new_node):
        if after_node is None:
            self.add_in_tail(new_node)
            return None

        node = self.__head.next
        while node is not self.__tail:
            if node == after_node:
                new_node.prev = node
                new_node.next = node.next
                node.next.prev = new_node
                node.next = new_node
                return None
            node = node.next
        return None
