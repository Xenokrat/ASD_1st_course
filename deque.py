class Deque:
    def __init__(self):
        self.array = []

    def addFront(self, item):
        self.array.insert(0, item)

    def addTail(self, item):
        self.array.append(item)

    def removeFront(self):
        if self.array:
            return self.array.pop(0)
        return None

    def removeTail(self):
        if self.array:
            return self.array.pop()
        return None

    def size(self):
        return len(self.array)