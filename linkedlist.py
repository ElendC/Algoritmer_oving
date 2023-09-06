 
#Q1. Write a program that finds and prints the minimum and maximum values in a singly linked list.
# >> So you need to create a singly linked list and populate it with some data.
# >> Write a function to find the min and max values.

    


class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __inti__(self):
        self.head = None

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


