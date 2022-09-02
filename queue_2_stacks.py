from stack import Stack


class QueueStacked:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if self.out_stack.size() == 0:
            while self.in_stack.size() > 0:
                itm = self.in_stack.pop()
                self.out_stack.push(itm)

        return self.out_stack.pop()

    def size(self):
        # size consists of size of 2 stacks combined
        return self.in_stack.size() + self.out_stack.size()
