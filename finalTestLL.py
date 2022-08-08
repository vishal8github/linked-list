#create singly linked list node
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        #initialize HEAD node
        self.head = Node()

    #------------------------------------------------------------
    #INSERT node AT the START of the linked list
    def insertAtStart(self, data):
        newNode = Node(data)

        temp = self.head.next

        self.head.next = newNode

        newNode.next = temp

    #INSERT node AT the END of the linked list
    def insertAtEnd(self, data):
        newNode = Node(data)
        curnt_node = self.head

        while curnt_node.next != None:
            curnt_node = curnt_node.next
        curnt_node.next = newNode

    #INSERT node AT perticular INDEX
    def insertDataAtIndex(self, index, data):
        if index >= self.length() or index <= -1:
            print("\n<ERROR: 'Insert': Index out of range !!! >")
            return
        newNode = Node(data)
        curnt_index = 0
        curnt_node = self.head
        while True:
            temp = curnt_node
            curnt_node = curnt_node.next
            if curnt_index == index:
                temp.next = newNode
                newNode.next = curnt_node
                break
            curnt_index += 1
                

    #------------------------------------------------------------
    #TRAVERSE through the linked list and find the length
    def length(self):
        curnt_node = self.head.next
        count = 0
        while curnt_node != None:
            count += 1
            curnt_node = curnt_node.next
        return count

    #------------------------------------------------------------
    #TRAVERSE through the linked list and display the data of nodes
    def display(self):
        elems = []

        curnt_node = self.head
        
        while curnt_node.next != None:
            curnt_node = curnt_node.next
            elems.append(curnt_node.data)
        print(f"\nLinked list: {elems}")

    #------------------------------------------------------------
    #TRAVERSE and get the data from perticular INDEX
    def getDataFromIndex(self, index):
        if index >= self.length() or index <= -1:
            return "<ERROR: 'Get': Index out of range !!! >"
        
        curnt_index = 0
        curnt_node = self.head
        while True:
            curnt_node = curnt_node.next
            if curnt_index == index:
                return curnt_node.data
            curnt_index += 1
    
    #------------------------------------------------------------
    #TRAVERSE and set the data to perticular INDEX
    def setDataToIndex(self, index, data):
        if index >= self.length() or index <= -1:
            print("<ERROR: 'Set': Index out of range !!! >")
        
        curnt_index = 0
        curnt_node = self.head
        while True:
            curnt_node = curnt_node.next
            if curnt_index == index:
                curnt_node.data = data
                break
            curnt_index += 1

    #------------------------------------------------------------
    #TRAVERSE and delete the data to perticular INDEX
    def delDataFromIndex(self, index):
        if index >= self.length() or index <= -1:
            print("\n<ERROR: 'Delete': Index out of range !!! >")
            return
        
        curnt_index = 0
        curnt_node = self.head
        while True:
            last_node = curnt_node
            curnt_node = curnt_node.next
            if curnt_index == index:
                last_node.next = curnt_node.next
                return
            curnt_index += 1



#Execution starts from here ***
my_list = LinkedList()

my_list.display()
print(f"Lenght of list: {my_list.length()}")

my_list.insertAtEnd(11)
my_list.insertAtEnd(22)
my_list.insertAtEnd(33)
my_list.insertAtEnd(44)
my_list.insertAtEnd(55)

my_list.display()
print(f"Lenght of list: {my_list.length()}")

my_list.insertAtStart(99)

my_list.display()
print(f"Lenght of list: {my_list.length()}")

print(f"\nGet data from index 2: {my_list.getDataFromIndex(2)}")

my_list.setDataToIndex(2, 70)

print(f"\nGet data from index 2: {my_list.getDataFromIndex(2)}")

print()
my_list.display()
my_list.delDataFromIndex(2)
print()
my_list.display()
print(f"Lenght of list: {my_list.length()}")

my_list.insertDataAtIndex(3, 888)

print()
my_list.display()
print(f"Lenght of list: {my_list.length()}")