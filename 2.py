class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self, *values):
        self.head = None
        for value in values:
            self.append(value)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print()

def remove_duplicates(circular_list):
    current = circular_list.head
    while True:
        duplicate_data = current.data
        runner = current.next

        while runner != current:
            if runner.data == duplicate_data:
                # Fjern noden runner da den inneholder en duplikat
                # Oppdater pekere for å hoppe over noden
                runner.prev.next = runner.next
                runner.next.prev = runner.prev
            runner = runner.next

        current = current.next
        if current == circular_list.head:
            break

# Create the list and remove duplicates
my_list = CircularDoublyLinkedList(1, 1, 1, 4, 3, 5, 5, 4, 3, 4, 3, 2)
remove_duplicates(my_list)

# Display the modified list
my_list.display()
