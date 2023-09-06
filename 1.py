
class Node:
    def __init__(self, data):
        self.data = data;              #The node value
        self.next = None;              #Empty value, will be replaced with a LinkedList object (containing a data and next)

class LinkedList:                       #tom linked list
    def __init__(self):
        self.head = None                #første nodeobject

    
    def addNode(self, data):            #Legger til ny node
        new_node = Node(data)           #calling Node class to create a new node
        new_node.next = self.head       #Gjør førsde node om til neste
        self.head = new_node            #Setter nye node inn som første node

    def print_linked_list(self):
        tempvar = self.head
        while tempvar.next != None:
            print(tempvar.data)
            tempvar = tempvar.next
        print(tempvar.data)

        
list = LinkedList()
list.addNode(2)
list.addNode(3)
list.addNode(4)
list.addNode(5)
list.addNode(6)
list.print_linked_list()

