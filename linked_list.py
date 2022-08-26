class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None  # pointer to first node
        self.tail = None  # pointer to last node

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        res = []
        node = self.head
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all=False):
        node = self.head
        parent = None  # here we save node parent
        is_first_found = False

        while node is not None:
            if is_first_found and not all:
                return None

            # if node has no parent then it's head
            if (node.value == val) and (parent is None):
                self.head = node.next
                node = node.next
                is_first_found = True
                continue

            elif (node.value == val) and (parent is not None):
                parent.next = node.next
                node = node.next
                is_first_found = True
                continue

            parent = node
            node = node.next

        if self.head is None:
            self.tail = None
            return None

        if parent.next is None:
            self.tail = parent
        else:
            self.tail = parent.next
        return None

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        counter = 0
        node = self.head
        while node is not None:
            counter += 1
            node = node.next
        return counter

    def insert(self, afterNode, newNode):

        # if list was empty
        if self.tail is None:
            newNode.next = None
            self.tail = newNode
            self.head = newNode
            return None

        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return None

        node = self.head
        while node is not None:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                break

            node = node.next

        # if newNode was inserted as last element
        if newNode.next is None:
            self.tail = newNode

        return None
