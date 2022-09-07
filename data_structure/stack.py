class Stack:
    def __init__(self):
        self.stack = []

    def add(self, val):
        if val not in self.stack:
            self.stack.append(val)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]


test_stack = Stack()
test_stack.add(1)
test_stack.add(2)
print(test_stack.peek())
test_stack.add(3)
test_stack.add(4)
print(test_stack.peek())
test_stack.remove()
print(test_stack.peek())
