import random

class Node:
    def __init__(self, data):
        self.data = data;              #The node value
        self.next = None;              #Empty value, will be replaced with a LinkedList object (containing a data and next)

class LinkedList:                       #tom linked list
    def __init__(self):
        self.head = None                #første nodeobject

    
    def addNode(self, data):           
        new_node = Node(data)           #calling Node class to create a new node
        new_node.next = self.head       #Gjør førsde node om til neste
        self.head = new_node            #Setter nye node inn som første node

    def print_linked_list(self):
        print("The Linked List:", end=" ")
        TheLinkedList = []
        cur_node = self.head
        while cur_node != None:
            TheLinkedList.append(str(cur_node.data))
            cur_node = cur_node.next
        print(" -> ".join(TheLinkedList))


    def max_value(self):
        maxV = self.head.data            #Første node til max node
        next_node = self.head.next       #Neste node
        while next_node != None: 
            if next_node.data > maxV:     
                maxV = next_node.data    
            next_node = next_node.next
        print("Max value: ", maxV)

    def min_value(self):
        minV = self.head.data
        next_node = self.head.next
        while next_node != None:
            if next_node.data < minV:
                minV = next_node.data
            next_node = next_node.next
        print("Lowest value: ", minV)
            
list = LinkedList()

for i in range(8):
    i = random.randint(1, 99)
    list.addNode(i)

list.print_linked_list()
list.max_value()
list.min_value()

