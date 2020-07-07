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

#COUNT OF LIST
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

#PRINTING THE VALUES OF LIST

    def printCircularList(self):
        currentNode = self.head
        if currentNode ==None:
            return 0
        print(currentNode.getData())
        currentNode = currentNode.getNext()
        if currentNode is not None:
            while currentNode != self.head:
                print (currentNode.getData())
                currentNode = currentNode.getNext()
                
#INSERT AT THE END OF LIST
    def insertAtEndlnCLL(self, data):
        current = self.head
        newNode = Node()
        newNode.setData(data)
        
        while current.getNext() !=self.head:
            current = current.getNext()
               
        newNode.setNext(newNode)
        if self.head== None:
            self.head =newNode;
        else:
            newNode.setNext(self.head)
            current.setNext(newNode)
            #self.head = newNode

#INSERT AT THE BEGINNING OF ILIST
    def insertAtBeginlnCLL (self, data):
        current=self.head
        newNode = Node()
        newNode.setData(data)
        if current is not None:
            while  current.getNext() != self.head:
                current = current.getNext()
                
        newNode.setNext(newNode)
        if self.head==None:
            self.head=newNode
        else:
            newNode.setNext(self.head)
            current.setNext(newNode)
            self.head = newNode
       


#CALLING THE FUNCTIONS
            
n=Node()

n.insertAtBeginlnCLL(1000)
n.insertAtBeginlnCLL(7)
n.insertAtEndlnCLL(6)
n.insertAtBeginlnCLL(5)
n.insertAtEndlnCLL(88)
n.insertAtEndlnCLL(99)

n.printCircularList()

count=n.circularListLength()
print("Count of list=",count)

