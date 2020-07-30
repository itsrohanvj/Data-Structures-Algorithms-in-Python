class Node:
    # If data is not given by user,ils taken as None
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        self.head = None
        self.length = 0
        self.tail=None
    # method for setting Lhe data field or I.he node
    def setData(self, data):
        self.data = data

    # method for getting the data field of the node
    def getData(self):
        return self.data

    # method for setting the next fie ld of the node
    def setNext(self, next):
        self.next = next

    # method for getting the next field of the node
    def getNext(self):
        return self.next

    # returns true if the node points to another node
    def hasNext(self):
        return self.next != None

    # method ror setting the next field of the node
    def setPrev(self, prev):
        self.prev = prev

    # method for getting the next field of the node
    def getPrev(self):
        return self.prev

    # returns true if the node points to another node
    def hasPrev(self):
        return self.prev != None

    # str returns string equivalent of Object
    def __str__(self):
        return "Node[Data = %s}" % (self.data,)

    # COUNT OF LIST
    def circularListLength(self):
        currentNode = self.head
        if currentNode == None:
            return 0
        self.count = 1
        currentNode = currentNode.getNext()
        while currentNode != self.head:
            currentNode = currentNode.getNext()
            self.count = self.count + 1
        return self.count

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

    # INSERT AT THE BEGINNING OF LIST
    def insertAtBeginlnCLL(self, data):

        newNode = Node(data, None, None)
        current = self.head
        if current is not None:
            while current.getNext() != self.head:
                current = current.getNext()

        newNode.setNext(newNode)
        newNode.setPrev(newNode)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.setPrev(current)
            newNode.setNext(current.getNext())
            current.getNext().setPrev(newNode)
            current.setNext(newNode)
            self.head = newNode

    def insertAtEndlnCLL(self, data):
        newNode = Node(data, None, None)
        current = self.head
        if current is not None:
            while current.getNext() != self.head:
                current = current.getNext()

        newNode.setNext(newNode)
        newNode.setPrev(newNode)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.setPrev(current)
            newNode.setNext(current.getNext())
            current.getNext().setPrev(newNode)
            current.setNext(newNode)
            self.tail=newNode
            # self.head = newNode  --THIS IS THE ONLY DIFF BETWEEN INSERT AT BEG v/s INSERT ATA END.

    # INSERT AT A PARTICULAR POSITION
    def getNode(self, index):
        currentNode = self.head
        #print("head=", self.head.getData())

        if currentNode == None:
            return None
        i = 2
        while i < index and currentNode is not self.tail:
            currentNode = currentNode.getNext()
            if currentNode == None:
                break
            i += 1
        return currentNode

    def insertAtPos(self, pos, data):
        z = self.circularListLength()
        if pos == 1:
            self.insertAtBeginlnCLL(data)
        elif pos==z+1:
            self.insertAtEndlnCLL(data)
        elif pos > z or pos < 1:
            print("Wrong Positional value , data passed=", data)
        else:
            temp = self.getNode(pos)  # calling of above function to find node.

            newNode = Node()
            newNode.setData(data)
            newNode.setNext(temp.getNext())
            newNode.setPrev(temp)
            temp.getNext().setPrev(newNode)
            temp.setNext(newNode)

    def deleteBeg(self):

        current=self.head
        z = self.circularListLength()
        if z == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            self.head.setPrev(self.head.getPrev())
            self.tail.setNext(self.head)


        # method to delete the last node of the linked list

    def deleteLast(self):
        z = self.circularListLength()
        if z == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head

            while currentnode.next != self.head:
                previousnode = currentnode
                currentnode = currentnode.next
            self.tail = previousnode
            previousnode.setNext(currentnode.next)
            currentnode.next.setPrev(self.tail)
            #previousnode.next = current

            self.length -= 1
        # at position

    def gettNode(self, index):
        z = self.circularListLength()
        if index > z or index < 1:
            return
        else:
            currentNode = self.head
            if currentNode == None:
                return None
            i = 1
            while i < index:
                currentNode = currentNode.getNext()
                if currentNode == None:
                    break
                i += 1
            return currentNode

    def deleteAtGivenPosition(self, index):

        temp = self.gettNode(index)
        if temp:
            if temp == self.head:
                self.deleteBeg()
            elif temp == self.tail:
                self.deleteLast()
            else:
                temp.getPrev().setNext(temp.getNext())
                if temp.getNext():
                    temp.getNext().setPrev(temp.getPrev())
            temp.setPrev(None)
            temp.setNext(None)
            temp.setData(None)

        # Deleting with given data

    def deleteValue(self, data):

        currentnode = self.head
        previousnode = self.head

        while currentnode.next != self.head:  # or currentnode.data != data:

            if currentnode.data == data:
                if self.head.data == data:
                    self.head = previousnode.next = currentnode.next
                    previousnode.next.setPrev(self.tail)
                    self.tail.next = previousnode.next  # = previousnode.next =currentnode.next
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

# CALLING THE FUNCTIONS
n = Node()

n.insertAtEndlnCLL("STRING VALUE")
n.insertAtBeginlnCLL(4989898989)
n.insertAtEndlnCLL(22222)
n.insertAtBeginlnCLL(99)
n.insertAtBeginlnCLL(990000)
n.insertAtBeginlnCLL(99999111)
n.insertAtPos(7, 6767676767)

n.printCircularList()
count=n.circularListLength()
print("count=",count)



print("\n After Delete\n")
n.deleteAtGivenPosition(2)
n.deleteBeg()
n.deleteLast()
n.deleteValue(99)
n.printCircularList()
count=n.circularListLength()
print("count=",count)



