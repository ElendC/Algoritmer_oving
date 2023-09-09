from datetime import datetime
import random
import os
import keyboard

class Task:
    def __init__(self, name, priority, due_date: datetime):  #due_date: datetime | after testing done
        self.name = str(name)
        self.priority = int(priority)
        self.due_date = due_date
        self.completed = False
        self.next = None

class LinkedListTasks:
    def __init__(self):
        self.head = None
    
    def addTask(self):
        #REMOVE FOR TESTING
        name = input("Whats you'r task: ")
        priority = int(input("Task priority: "))
    
        while True:
            due_date_input = input("Due date (yyyy-mm-dd): ")
            try:
                due_date = datetime.strptime(due_date_input, '%Y-%m-%d')
                break
            except ValueError:
                print("Date needs to be in form YYYY-MM-DD")

        #REMOVE FOR TESTING

        # JUST FOR TESTING
        # name = str(random.randint(1,10))
        # priority = random.randint(10, 20)
        # due_date = random.randint(50, 100)
        # JUST FOR TESTING

        new_task = Task(name, priority, due_date)
        new_task.next = self.head
        self.head = new_task

        print("\n")
        print("Your Task list now contains: ")
        self.printLinkedList()
      

    def printLinkedList(self):
        list = []
        currentTask = self.head
        while currentTask:
            list.append(currentTask.name)
            currentTask = currentTask.next
        print(f"Your Tasks: {list}")
        print("\n")
      
    def deleteTask(self):
        if self.head is None:
            print("List is empty")
            print("Press y to contiune")
            keyboard.wait("y")
            print("\n")
            print("Your Task List now contains: ")
            self.printLinkedList()
            print("Press y to contiune")
            print("\n")
            keyboard.wait("y")
            return
        
        delete_name = input("Which task would you like to delete: ")
        currentTask = self.head

        if currentTask.name == delete_name:
            self.head = currentTask.next

        while currentTask:
            if currentTask.next is not None and currentTask.next.name == delete_name:
                currentTask.next = currentTask.next.next

            else:
                currentTask = currentTask.next
        
    def viewTask(self, taskName):
        currentTask = self.head
        while currentTask:
            if currentTask.name == taskName:
                print(f"Task: {currentTask.name} | Completed: {currentTask.completed} | Task Priority: {currentTask.priority} | Due date:{currentTask.due_date}")  # noqa: E501
                currentTask = currentTask.next
            else:
                currentTask = currentTask.next
    
    def completed(self, taskName):
        currentTask = self.head
        while currentTask:
            if currentTask.name == taskName:
                currentTask.completed = True
                break
            currentTask = currentTask.next
        
        
class Menu:
    def __init__(self, linkedList):
        self.linkedList = linkedList

    def displayMenu(self):
        while True:   
            # keyboard.wait("y")
            list = ["Add", "Delete", "Display List", "View Task", "Complete Task" ,"Clear Log", "Exit"]  # noqa: E501
            print("Menu: ", end=" ")
            for i in range(len(list)):
                print(list[i],":", i+1 , end=" | ")
            selected = input("\nSelect: ")
            
            if selected == "1":
                self.linkedList.addTask()
            
            elif selected == "2":
                self.linkedList.deleteTask()

            elif selected == "3":
                self.linkedList.printLinkedList()
                
            elif selected == "4":
                k = str(input("which task would you display: "))
                self.linkedList.viewTask(k)
                print("Press space to contiune")
                keyboard.wait("space")
                
            elif selected == "5":
                k = input("Task Name: ")
                self.linkedList.completed(k)
                
            elif selected == "6":
                os.system('cls')

            elif selected == "7":
                break


            else:
                print("Please chose a valid number, y to contiune \n")
            
            


# list = LinkedListTasks()
# for i in range(6):
#     list.addTask()
# list.printLinkedList()


startapp = Menu(LinkedListTasks())
startapp.displayMenu()
