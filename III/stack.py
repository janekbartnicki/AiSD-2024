class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def add(self, element):
        self.stack.append(element)

    def next(self):
        if self.is_empty():
            return None

        return self.stack.pop()

    def find(self, element):
        for index, item in enumerate(self.stack):
            if item == element:
                return index

        return None


stack = Stack()

stack.add(1)
stack.add(2)
stack.add(3)
stack.add(4)

print(stack.next())
print(stack.find(2))