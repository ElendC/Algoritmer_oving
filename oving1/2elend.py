import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class CircDublyLinkedList:
    def __init__(self):
        self.head = None
    
    def addNode(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = self.head.prev   

            self.head.prev.next = new_node  
            self.head.prev = new_node

    def printList(self):
        cur_node = self.head
        circList = []
        while True:
            circList.append(str(cur_node.data))
            cur_node = cur_node.next
            if cur_node is self.head:
                break
        print(" <-> ".join(circList))

    def checkDoubles(self):
        currentNode = self.head
        
        while currentNode.next != self.head:             #går gjennom alle frem til siste
            comparingNode = currentNode.next             #neste node er den vi sammenligner med
            while comparingNode != self.head:            #skjekker comparingNode med alle til siste
                if currentNode.data == comparingNode.data:
                    comparingNode.prev.next = comparingNode.next
                    comparingNode.next.prev = comparingNode.prev
                    
                comparingNode = comparingNode.next

            currentNode = currentNode.next
        self.printList()

list = CircDublyLinkedList()

for i in range(10):
    i = random.randint(1, 5)
    list.addNode(i)   
print("The Dubbly circular linked list: ")
list.printList()
print("\n")
print("Removed Dublicates: ")
list.checkDoubles()

