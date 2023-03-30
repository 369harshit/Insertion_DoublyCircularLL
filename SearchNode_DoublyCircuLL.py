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

    # Search an element in the list
    def SearchElement(self, searchValue):
        temp = self.head
        found = 0
        i = 0

        if temp is not None:
            while True:
                i += 1
                if temp.data == searchValue:
                    found += 1
                    break
                temp = temp.next
                if temp == self.head:
                    break
            if found == 1:
                print(searchValue, "is found at index =", i)
            else:
                print(searchValue, "is not found in the list.")
        else:
            print("The list is empty.")

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

# search for element in the list
MyList.SearchElement(10)
MyList.SearchElement(15)
MyList.SearchElement(20)
