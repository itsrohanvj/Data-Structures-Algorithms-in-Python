#Node of a Circular Linked List
class Node:
#constructor
    def __init__(self):
        self.data= None
        self.next = None
        self.head=None
        self.count=0
    #method for setting the data field of the node
    def setData(self,data):
        self.data= data
    #method for getting the data field of the node
    def getData(self):
        return self.data
    #method for setting the next field of the node
    def setNext(self,next):
        self.next= next
    #method for getting the next field of the node
    def getNext(self):
        return self.next
    #returns true if the node points to another node
    def hasNext(self):
        return self.next != None

#COUNT OF LIST
    def circularListLength(self):
        currentNode = self.head
        if currentNode ==None:
            return 0
        self.count =1
        currentNode = currentNode.getNext()
        while currentNode != self.head:
            currentNode = currentNode.getNext()
            self.count = self.count+ 1
        return self.count

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

#INSERT AT THE BEGINNING OF LIST
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

#INSERT AT A PARTICULAR POSITION
    def  insertAtPos(self,pos,data):
        if pos==0:
            self.insertAtBeginlnCLL(data)
        elif pos>self.count or pos<0:
            print("Wrong Positional value")
        else:
            current=self.head
            newNode = Node()
            newNode.setData(data)
            for i in range(0,pos-2):
                current = current.getNext()
            newNode.setNext(current.getNext())
            current.setNext(newNode)
#CALLING THE FUNCTIONS
            
n=Node()

n.insertAtBeginlnCLL(657)
n.insertAtBeginlnCLL(7)
n.insertAtEndlnCLL(6)
n.insertAtBeginlnCLL(5)
n.insertAtEndlnCLL(88)
n.insertAtEndlnCLL(99)

n.circularListLength() #this function is called twice because the count is done after adding all the nodes.
n.insertAtPos(4,1000) # the above count is used to find the position.
count=n.circularListLength() # alternative of above: use counter variable after adding every node
n.printCircularList()
print("Count of list=",count)

