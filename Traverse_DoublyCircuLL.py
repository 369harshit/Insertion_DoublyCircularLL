# node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# class Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Add new element at the end of the list
    def push_back(self, newElement):
        newNode = Node(newElement)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            newNode.prev = self.head
            return
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head
            newNode.prev = temp
            self.head.prev = newNode

    # display the content of the list
    def PrintList(self):
        temp = self.head
        if temp is not None:
            print("The list contains:", end=" ")
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break
            print()
        else:
            print("The list is empty.")


# test the code                  
MyList = LinkedList()

# Add three elements at the end of the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)

# traverse to display the content of the list.
MyList.PrintList()
