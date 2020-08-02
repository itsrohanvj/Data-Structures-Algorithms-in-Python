# Node of a Circulur Linked List
class Node:
    # constructor
    def __init__(self):
        self.data = None
        self.next = None
        self.head = None
        self.last=None
        self.length = 0

    # melhod for setting the data field of the node
    def setData(self, data):
        self.data = data

    # method for getting the data field of the node
    def getData(self):
        return self.data

    # melhod for setting the next field of the node
    def setNext(self, next):
        self.next = next

    # method for getting Lhc next field of the node
    def getNext(self):
        return self.next

    # returns true if Lhc node points to anolher node
    def hasNext(self):
        return self.next != None

    # COUNT OF LIST
    def circularListLength(self):
        currentNode = self.head
        if currentNode == None:
            return 0
        count = 1
        currentNode = currentNode.getNext()
        while currentNode != self.head:
            currentNode = currentNode.getNext()
            count = count + 1
        return count

    # PRINTING THE VALUES OF LIST

    def printCircularList(self):
        currentNode = self.head
        if currentNode == None:
            return 0
        print(currentNode.getData())
        currentNode = currentNode.getNext()
        if currentNode is not None:
            while currentNode != self.head:
                print(currentNode.getData())
                currentNode = currentNode.getNext()

    # INSERT AT THE END OF LIST
    def insertAtEndlnCLL(self, data):
        current = self.head
        self.last=newNode = Node()
        newNode.setData(data)

        while current.getNext() != self.head:
            current = current.getNext()

        newNode.setNext(newNode)
        if self.head == None:
            self.head = newNode;

        else:
            newNode.setNext(self.head)
            current.setNext(newNode)
        self.length+=1

    # INSERT AT THE BEGINNING OF ILIST
    def insertAtBeginlnCLL(self, data):
        current = self.head
        newNode = Node()
        newNode.setData(data)
        if current is not None:
            while current.getNext() != self.head:
                current = current.getNext()

        newNode.setNext(newNode)
        if self.head == None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            current.setNext(newNode)
            self.head = newNode
        self.length += 1


    def insertAtPos(self, pos, data):
        if pos > self.length or pos < 1:
            return None
        else:
            if pos == 1:
                self.insertAtBeginlnCLL(data)
            elif pos==self.length:
                self.insertAtEndlnCLL(data)

            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    count = 1
                    current = self.head
                    while count < pos - 1:
                        count += 1
                        current = current.getNext()
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self.length += 1

   #delete the first node.
    def deleteBeg(self):
        current =self.head
        if self.head is None:
            print("The list is empty")
            return
        while current.getNext()!=self.head:
            current=current.getNext()
        current.setNext(self.head.getNext())
        self.head=self.head.getNext()
        return

    # method to delete the last node of the linked list
    def deleteLast(self):

        temp=self.head
        current=self.head
        if self.head==None:
            print("List empty")
            return
        while current.getNext()!=self.head:
            temp=current
            current=current.getNext()
        temp.setNext(current.getNext())
        self.last=temp
        return

    def deleteValue(self, data):

        currentnode = self.head
        previousnode = self.head

        while currentnode.next != self.head:  # or currentnode.data != data:

            if currentnode.data == data:
                if self.head.data == data:
                    self.head = previousnode.next = currentnode.next
                    self.last.next=self.head #= previousnode.next =currentnode.next
                else:
                    previousnode.next = currentnode.next
                self.length -= 1
                return

            else:
                previousnode = currentnode
                currentnode = currentnode.next

        if currentnode.next == self.head and currentnode.data == data:
            previousnode.next = currentnode.next
            self.length -= 1


    # method to delete a node at a particular position
    def deleteAtPos(self, pos):
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        # to delete the first position of the linkedlist
        elif pos == 1:
            self.deleteBeg()
        # to delete the last position of the linkedlist
        elif pos== self.length:
            self.deleteLast()
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next

# CALLING THE FUNCTIONS

n = Node()

n.insertAtBeginlnCLL(1000)
n.insertAtBeginlnCLL(7)
n.insertAtEndlnCLL(6)
n.insertAtBeginlnCLL(5)
n.insertAtEndlnCLL(88)
n.insertAtEndlnCLL(99)
n.insertAtPos(4,567)


n.printCircularList()

count = n.circularListLength()
print("Count of list=", count)

print("\n After Delete\n")
n.deleteBeg()
n.deleteLast()
n.deleteAtPos(3)
n.deleteValue(88)
n.printCircularList()


count = n.circularListLength()
print("Count of list=", count)




