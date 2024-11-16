class DoublyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = DoublyLinkedNode(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        new_node.prev = current
        current.next = new_node

    def delete(self, value_to_delete):
        if self.head is None:
            return
        if self.head.value == value_to_delete:
            self.head = self.head.next
            self.head.prev = None
            return

        current = self.head

        while current:
            if current.value == value_to_delete:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next

    def find(self, searched_element):
        current = self.head
        while current:
            if current.value == searched_element:
                return current
            current = current.next
        return None

    def insert(self, index, inserted_value):
        if index == 0:
            new_node = DoublyLinkedNode(inserted_value)
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        new_node = DoublyLinkedNode(inserted_value)
        current = self.head
        steps = 0

        while current:
            if steps == index - 1:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            steps += 1
            current = current.next

        self.add(inserted_value)


doubly_linked_list = DoublyLinkedList()

doubly_linked_list.add('A')
doubly_linked_list.add('B')
doubly_linked_list.add('C')
doubly_linked_list.add('D')
doubly_linked_list.add('E')
doubly_linked_list.add('F')

doubly_linked_list.delete('C')

current = doubly_linked_list.head
while current:
    print(current.value)
    current = current.next

print()
print(f'Node with searched value: {doubly_linked_list.find('B')}', end='\n\n')

doubly_linked_list.insert(3, 'R')

current = doubly_linked_list.head
while current:
    print(current.value)
    current = current.next