class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        res = []
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all=False):
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

        return None

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        len_ = 0
        while node is not None:
            len_ += 1
            node = node.next
        return len_

    def insert(self, afterNode, newNode):
        if (afterNode is None) or (afterNode == self.tail):
            self.add_in_tail(newNode)
            return None

        node = self.head
        while node is not None:
            if node == afterNode:
                node.next.prev = newNode
                node.next = newNode
                newNode.prev = node
                newNode.next = node.next
            node = node.next

        return None

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
