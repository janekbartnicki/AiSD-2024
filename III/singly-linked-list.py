class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node

    def delete(self, searched_value):
        if self.head is None:
            return
        if self.head.value == searched_value:
            self.head = self.head.next
            return

        current = self.head

        while current.next:
            if current.next.value == searched_value:
                current.next = current.next.next
                return

            current = current.next


    def find(self, searched_element):
        current = self.head

        while current:
            if current.value == searched_element:
                return current
            current = current.next

        return None

    def insert(self, index, value):
        new_node = Node(value)

        if index == 0:  # Wstawienie na początek listy
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        steps = 0

        while current:
            if steps == index - 1:
                next_node = current.next
                current.next = new_node
                new_node.next = next_node
                return
            steps += 1
            current = current.next

        self.add(value)


singly_linked_list = SinglyLinkedList()

singly_linked_list.add('A')
singly_linked_list.add('B')
singly_linked_list.add('C')

current = singly_linked_list.head

while current:
    print(current.value)
    current = current.next

print()
current = singly_linked_list.head
singly_linked_list.delete('B')

while current:
    print(current.value)
    current = current.next

print(f'Node with searched value: {singly_linked_list.find('A')}')
print()

singly_linked_list.insert(2, 'B')

current = singly_linked_list.head
while current:
    print(current.value)
    current = current.next