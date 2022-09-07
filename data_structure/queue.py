class Queue:
    def __init__(self):
        self.queue = list()

    def add(self, val):
        if val not in self.queue:
            self.queue.insert(0, val)
            return True
        return False

    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")

    def size(self):
        return len(self.queue)

    def peek(self):
        return self.queue[-1]


test_queue = Queue()
test_queue.add(1)
test_queue.add(2)
test_queue.add(3)
test_queue.add(4)
test_queue.remove()
print(test_queue.peek())
# print(test_queue.size())
