class StackReverse:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop(0)

    def push(self, value):
        self.stack = [value] + self.stack

    def peek(self):
        if not self.stack:
            return None
        return self.stack[0]
