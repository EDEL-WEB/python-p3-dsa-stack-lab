class Stack:
    def __init__(self, items=None, limit=10):
        self.items = items if items is not None else []
        self.limit = limit

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        """Return how far `target` is from the top of the stack. Top = 0."""
        if target in self.items:
            return self.items[::-1].index(target)
        return -1
