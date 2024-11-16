class CircularLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add(self, value):
        new_node = CircularLinkedListNode(value)
        new_node.next = self.head

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.tail.next = self.head


    def delete(self, searched_value):
        if self.head is None:
            return

        if self.head.value == searched_value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            return

        current = self.head
        while current.next != self.head:
            if current.next.value == searched_value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.tail.next = self.head
                return
            current = current.next


    def insert(self, index, value):
        new_node = CircularLinkedListNode(value)

        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                self.tail.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
            return

        current = self.head
        counter = 0

        while current.next != self.head:
            if counter + 1 == index:
                new_node.next = current.next
                current.next = new_node

                if current == self.tail:
                    self.tail = new_node
                return
            current = current.next
            counter += 1

        if counter + 1 == index:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head


    def find(self, searched_value):
        if self.head is None:
            return None

        current = self.head
        counter = 0

        while True:
            if current.value == searched_value:
                return counter
            current = current.next
            counter += 1
            if current == self.head:
                break

        return None


circular_linked_list = CircularLinkedList()

circular_linked_list.add('A')
circular_linked_list.add('B')
circular_linked_list.add('C')
circular_linked_list.add('D')
circular_linked_list.add('E')
circular_linked_list.add('F')

circular_linked_list.delete('B')

circular_linked_list.insert(3, 'X')

current = circular_linked_list.head
while True:
    print(current.value)
    current = current.next
    if current == circular_linked_list.head:
        break