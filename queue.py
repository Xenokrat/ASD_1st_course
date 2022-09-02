class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, item):
        self.array.insert(0, item)

    def dequeue(self):
        if not self.array:
            return None
        return self.array.pop()

    def size(self):
        return len(self.array)
