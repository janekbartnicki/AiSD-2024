class PriorityQueue:
    def __init__(self):
        self.priority_queue = []

    def add(self, element, priority):
        self.priority_queue.append(
            (element, priority)
        )

    def is_empty(self):
        return len(self.priority_queue) == 0

    def next(self):
        if self.is_empty():
            return None

        min_priority_value = self.priority_queue[0][1]
        min_priority_value_index = 0

        for index, item in enumerate(self.priority_queue):
            if int(item[1]) < min_priority_value:
                min_priority_value = item[1]
                min_priority_value_index = index

        return self.priority_queue.pop(min_priority_value_index)

    def find(self, element):
        for index, item in enumerate(self.priority_queue):
            if item[0] == element:
                return index

        return None


priority_queue = PriorityQueue()

priority_queue.add('apple', 6)
priority_queue.add('banana', 1)
priority_queue.add('orange', 3)

print(f'Index of banana: {priority_queue.find('banana')}')

print(priority_queue.next())
print(priority_queue.next())
print(priority_queue.next())
