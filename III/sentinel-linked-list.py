class SentinelLinkedListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SentinelLinkedList:
    def __init__(self):
        self.sentinel = SentinelLinkedListNode()

    def add(self, value):
        new_node = SentinelLinkedListNode(value)
        current = self.sentinel
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        current = self.sentinel
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def find(self, value):
        current = self.sentinel.next
        while current:
            if current.value == value:
                return current
            current = current.next
        return None


sentinel_linked_list = SentinelLinkedList()

sentinel_linked_list.add('A')
sentinel_linked_list.add('B')
sentinel_linked_list.add('C')
sentinel_linked_list.add('D')
sentinel_linked_list.add('E')
sentinel_linked_list.add('F')

sentinel_linked_list.delete('B')

current = sentinel_linked_list.sentinel.next
while current:
    print(current.value)
    current = current.next
