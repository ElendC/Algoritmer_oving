class Node:
 def __init__(self, data):
   self.data = data
   self.next = None

class LinkedList:
  def __init(self):
    self.head = None

  def printlist(self):
    temp = self.head
    if (temp != None):
      print('list contains: ')
      while(temp != None):
        print(temp.data, end = ' > ')
        temp = temp.next
      print("\n")
    else:
      print('List is empty')

  def pushfront(self, data):
     node = Node(data)
     temp = self.head
     node.next = temp
     self.head = node

  def pushback(self, data):
    newnode = Node(data)
    temp = self.head
    while(temp.next != None):
        temp = temp.next
    temp.next = newnode

  def remove_front(self):
    temp = self.head
    self.head = temp.next
    temp = None

  def remove_back(self):
     temp = self.head
     while(temp.next.next != None):
        temp = temp.next
     temp.next = None

  def len_of_list(self):
    temp = self.head
    len = 0
    while(temp != None):
      temp = temp.next
      len += 1
    return len

  def push_at(self, data, position):
    newnode = Node(data)
    leng = self.len_of_list()

    if position == 1:
      self.pushfront(data)

    elif position > leng:
      print('out of range')

    else:
       position -= 1
       temp = self.head
       for i in range(position):
        temp = temp.next

       newnode.next = temp.next.next
       temp.next = newnode


  def push_at_by_index(self, data, index):
    newnode = Node(data)
    leng = self.len_of_list()

    if index == 0:
      self.pushfront(data)

    elif index > leng:
      print('out of range')

    else:
      temp = self.head
      i = 1
      while(i < index):
        temp = temp.next
        i += 1
      newnode.next = temp.next
      temp.next = newnode


  def search(self, x):
    temp = self.head
    while(temp != None):
      if temp.data == x:
        return True
      temp = temp.next
    return False

  def count(self, x):
     temp = self.head
     count = 0

     while(temp != None):
       if temp.data == x:
        count += 1
       temp = temp.next
     return count

  def getminmax(self):
    temp = self.head
    min = self.head.data
    max = self.head.data
    while(temp != None):
      if (temp.data < min):
        min = temp.data
      elif (temp.data > max):
        max = temp.data
      temp = temp.next
    return min, max

# 10>20>30>40>50
# 50>40>30>20>10
  def reverse(self):
    temp = self.head
    prev = None
    while(temp != None):
           next_node = temp.next
           temp.next = prev
           prev = temp
           temp = next_node
    self.head = prev


mylist = LinkedList()

node1 = Node(10)
mylist.head = node1

node2 = Node(20)
node1.next = node2

node3 = Node(30)
node2.next = node3

node4 = Node(40)
node3.next = node4

mylist.printlist()

mylist.pushfront(5)
mylist.printlist()

mylist.pushback(50)
mylist.printlist()

mylist.pushback(60)
mylist.printlist()

mylist.remove_front()
mylist.printlist()

mylist.remove_back()
mylist.printlist()

print('len of the list is: ', mylist.len_of_list())

mylist.push_at_by_index(25,0)
mylist.printlist()

mylist.push_at_by_index(25,3)
mylist.printlist()

mylist.push_at_by_index(25,2)
mylist.printlist()


mylist.search(100)

mylist.count(50)

print(mylist.getminmax())


mylist.reverse()


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoubleLinkedList:
  def __init(self):
    self.head = None

  def printlist(self):
    temp = self.head
    if (temp != None):
      print('list contains: ')
      while(temp != None):
        print(temp.data, end = ' > ')
        temp = temp.next
      print("\n")
    else:
      print('List is empty')


first = Node(10)
second = Node(20)
third = Node(30)
mylist = DoubleLinkedList()
mylist.head = first

#10>20>30
first.next = second
first.prev = None

second.next = third
second.prev = first

third.next = None
third.prev = second


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class circularsingleLinkedList:
  def __init(self):
    self.head = None

  def printlist(self):
    temp = self.head
    if (temp != None):
      print('list contains: ')
      while(temp.next != self.head ):
        print(temp.data, end = ' > ')
        temp = temp.next

      print(temp.data)
      print("\n")
    else:
      print('List is empty')

first = Node(10)
second = Node(20)
third = Node(30)

mylist = circularsingleLinkedList()
mylist.head = first
#10>20>30
first.next = second
second.next = third
third.next = first

mylist.printlist()
