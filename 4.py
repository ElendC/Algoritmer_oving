from datetime import datetime
import random
import string
import keyboard

class Task:
    def __init__(self, name, priority, due_date):  #due_date: datetime | after testing done
        self.name = str(name)
        self.priority = int(priority)
        self.due_date = due_date
        self.completet = False
        self.next = None


class LinkedListTasks:
    def __init__(self):
        self.head = None
    
    def addTask(self):
        # name = input("Whats you'r task: ")
        # priority = int(input("Task priority: "))
        # due_date_input = input("Due date (yyyy:mm:dd): ")
        # due_date = datetime.strptime(due_date_input, '%Y-%m-%d')

        # JUST FOR TESTING
        letters = "eariotnslh"
        name = str(random.randint(1,10))
        priority = random.randint(1, 20)
        due_date = random.randint(50, 100)
        # JUST FOR TESTING

        new_task = Task(name, priority, due_date)
        new_task.next = self.head
        self.head = new_task


    def printLinkedList(self):
        list = []
        currentTask = self.head
        while currentTask:
            list.append(currentTask.name)
            currentTask = currentTask.next
        print(f"Your Tasks: {list}")

    def deleteTask(self):
        delete_name = input("Which task would you like to delete: ")
        currentTask = self.head

        if self.head == None:
            print("List is empty")
            return

        if currentTask.name == delete_name:
            self.head = currentTask.next

        while currentTask:
            if currentTask.next is not None and currentTask.next.name == delete_name:
                currentTask.next = currentTask.next.next

            else:
                currentTask = currentTask.next
        

class Menu:
    def __init__(self, linkedList):
        self.linkedList = linkedList

    def displayMenu(self):
        while True:
            
            keyboard.wait("space")

          
            list = ["Add", "Delete", "Display", "Quit"]
            for i in range(len(list)):
                print(i+1, list[i])
            selected = input("Select: ")

            if selected == "1":
                self.linkedList.addTask()
            
            if selected == "2":
                self.linkedList.deleteTask()

            if selected == "3":
                self.linkedList.printLinkedList()

            if selected == "4":
                break
        


# list = LinkedListTasks()
# for i in range(6):
#     list.addTask()
# list.printLinkedList()
#test

startapp = Menu(LinkedListTasks())
startapp.displayMenu()
