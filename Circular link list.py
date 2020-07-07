#Node of a Circulur Linked List
class Node:
#constructor
    def __init__(self):
        self.data= None
        self.next = None
        self.head=None
        self.length=0
    #melhod for setting the data field of the node
    def setData(self,data):
        self.data= data
    #method for getting the data field of the node
    def getData(self):
        return self.data
    #melhod for setting the next field of the node
    def setNext(self,next):
        self.next= next
    #method for getting Lhc next field of the node
    def getNext(self):
        return self.next
    #returns true if Lhc node points to anolher node
    def hasNext(self):
        return self.next != None

#This method would be a member of other etass (say, CircularList)
    def circularListLength(self):
        currentNode = self.head
        if currentNode ==None:
            return 0
        count =1
        currentNode = currentNode.getNext()
        while currentNode != self.head:
            currentNode = currentNode.getNext()
            count = count+ 1
        return count



    def printCircularList(self):
        currentNode = self.head
        if currentNode ==None:
            return 0
        print(currentNode.getData())
        currentNode = currentNode.getNext()
        if currentNode!= None:
            while currentNode != self.head:
                currentNode = currentNode.getNext()
            print (currentNode.getData())



    def insertAtEndlnCLL(self, data):
        current=self.head
        newNode = Node()
        newNode.setData(data)
        
        if current!= None:
            
            while  current.getNext() != self.head:
                current = current.getNext()
            current.setNext(newNode)
        else:
            newNode.setNext(self.head)
            current.setNext(newNode)


    def insertAtBeginlnCLL (self, data):
        current=self.head
        newNode = Node()
        newNode.setData(data)
        
       # print(current.getNext())
        if current is not None:
            while  current.getNext() != self.head:
                current = current.getNext()
        
            current.setNext(newNode)
        
        else:
            newNode.setNext(self.head)
            newNode.setNext(newNode)
        self.head = newNode
       



n=Node()
#n.insertAtBeginlnCLL(5)

n.insertAtBeginlnCLL(6)
n.insertAtBeginlnCLL(7883830)


n.insertAtBeginlnCLL(700)
#n.insertAtEndlnCLL(990)
#n.insertAtEndlnCLL(6)
n.printCircularList()
