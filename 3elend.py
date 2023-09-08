import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head=newNode

    def printList(self):
        currNode = self.head
        nodeList = []
        while currNode != None:
            nodeList.append(str(currNode.data))
            currNode = currNode.next
        
        print("->".join(nodeList))

    def swapper(self, k):
            count = 0
            temp = self.head
            while temp != None:
                 count += 1
                 temp = temp.next
            print("count is: ",count)
            if k > count/2:
                 return print("K value needs to be less than half the list")
            
            temp1 = self.head
            temp2 = self.head

            for i in range(k-1):
                temp1 = temp1.next   #temp1 is now node nr k

            for i in range(count-k):      
                 temp2 = temp2.next  #temp2 is now k-th last node
            
            for i in range(k):
                 temp1.data, temp2.data = temp2.data, temp1.data
                 temp1 = temp1.prev if temp1.prev else temp1.next  #Dersom det er head
                 temp2 = temp2.next if temp2.next else temp2.prev  #dersom last node
                 



list = DoublyLinkedList()
for i in range(6):
     i = random.randint(1, 6)
     list.addNode(i)

list.printList()
list.swapper(2)
list.printList()