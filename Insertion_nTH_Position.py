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

    # Inserts a new element at the given position
    def push_at(self, newElement, position):
        newNode = Node(newElement)
        temp = self.head
        NoOfElements = 0
        if temp is not None:
            NoOfElements += 1
            temp = temp.next
        while temp != self.head:
            NoOfElements += 1
            temp = temp.next

        if position < 1 or position > (NoOfElements + 1):
            print("\nInvalid position.")
        elif position == 1:
            if self.head is None:
                self.head = newNode
                self.head.next = self.head
                self.head.prev = self.head
            else:
                while temp.next != self.head:
                    temp = temp.next
                temp.next = newNode
                newNode.prev = temp
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

        else:
            temp = self.head
            for i in range(1, position - 1):
                temp = temp.next
            newNode.next = temp.next
            newNode.next.prev = newNode
            newNode.prev = temp
            temp.next = newNode

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
MyList.PrintList()

# Insert an element at position 2
MyList.push_at(100, 2)
MyList.PrintList()

# Insert an element at position 1
MyList.push_at(200, 1)
MyList.PrintList()
