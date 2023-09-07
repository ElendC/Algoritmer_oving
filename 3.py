#Q3. Write a program that reads the K value as an input and swaps the first K nodes with the last K nodes in a doubly linked list


#Konstruerer klassen node som lager individuelle elementer med data ok pekere.
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

#Konstruerer en klasse som representerer dobbelt lenke liste som berstår av noder.
class DoublyLinkedList:

    def __init__(self, *values):  # Metoden tar en vilkårlig mengde argumenter (*values)
        self.head = None          # self.head representerer start noden.
        for value in values:      # forløkke som går igjennom alle *values
            self.append(value)    # oppretter ny node med verdien value

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print()




# Lager liste
my_list = DoublyLinkedList(1, 1, 1, 4, 3, 5, 5, 4, 3, 4, 3, 2, 8,7,9,9)


my_list.display()