class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None
    
    def viewList(self):
        if self.start == None:
            print("Empty Linked-list !!!")
        else:
            temp = self.start
            while temp != None:
                print(temp.data, end=' ')
                temp = temp.next

    def deleteFirst(self):
        if self.start == None:
          print("Empty Linked-list !!!")
        else:
            self.start = self.start.next

    def insertLast(self, value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode


mylist = LinkedList()

mylist.insertLast(11)
mylist.insertLast(22)
mylist.insertLast(33)
mylist.insertLast(44)

mylist.viewList()
print()

mylist.deleteFirst()

mylist.viewList()
