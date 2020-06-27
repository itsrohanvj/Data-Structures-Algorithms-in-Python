    #Node of a Singly Linked List
class Node:
#constructor
    def __init__ (self):
            self.data = None
            self.next = None
            self.length=0
            self.head=None
#method for setting the data field of the node
    def setData(self,data):
            self.data = data
#method for getting the data field of the node
    def getData(self):
            return self.data
#method for setting the next field of the node
    def setNext(self,next):
                self.next = next
#method for getting the next field of the node
    def getNext(self):
            return self.next
#returns trne if the node points to another node
    def hasNext(self):
            return self.next != None
#TO GET LENGTH OF LIST AND ALSO PRINT VALES
    
    def listLength(self):
        current = self.head
        
        count=0
        while  current!=None:
            count=count+1
            p=current.hasNext()
            
            print(current.getData())
            current = current.getNext()
            
    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head= newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1

    def insertAtEnd(self,data):
        newNode = Node()
        newNode.setData(data)
        current= self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(newNode)
        self.length+=1

    def insertAtPos(self,pos,data):
        
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBeg(data)
            else:
                if pos ==self.length :
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    count= 0
                    current= self.head
                    while count< pos-1:
                        count+=1
                        current = current.getNext()
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self.length += 1
                
#CALLING FUNCTIONS
n=Node()
n.insertAtBeginning(4)
n.insertAtEnd(5)
n.insertAtEnd(7)
n.insertAtPos(1,99)

n.listLength()













        
