class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def add(self, element):
        self.queue.append(element)

    def next(self):
        if self.is_empty():
            return None

        return self.queue.pop(0)

    def find(self, searched_element):
        for index, queue_element in enumerate(self.queue):
            if searched_element == queue_element:
                return index

        return None

queue = Queue()

queue.add(5)
queue.add(6)
queue.add(7)

print(queue.next())
print(queue.find(6))