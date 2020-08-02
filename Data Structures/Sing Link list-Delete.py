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

    
    def listLength(self):
        print("length=",self.length)
        current = self.head
        
        count=0
        while  current!=None:
            count=count+1
            p=current.hasNext()
            
            print(current.getData())
            
            current = current.getNext()
        print("count=",count)
            
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
        if (self.head == None): #To imply that if head == None
            newNode = Node()
            newNode.setData(data)
            self.head=newNode
            self.length+=1
        
        else:
            
            current= self.head
            while current.getNext() != None:
                current = current.getNext()
            newNode = Node()
            newNode.setData(data)    
            current.setNext(newNode)
            self.length+=1

    def insertAtPos(self,pos,data):
        if pos > self.length or pos < 1:
            return None
        else:
            if pos == 1:
                self.insertAtBeginning(data)
                
            else:
                if pos ==self.length :
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    count= 1
                    current= self.head
                    while count< pos-1:
                        count+=1
                        current = current.getNext()
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self.length += 1


        

    def deleteBeg(self):
        if self.length == 0:
            print ("The list is empty")
        else:
            self.head = self.head.next
            self.length -= 1
     
    # method to delete the last node of the linked list
    def deleteLast(self):
         
        if self.length == 0:
            print ("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head
             
            while currentnode.next != None:
                previousnode = currentnode
                currentnode = currentnode.next
                 
            previousnode.next = None
             
            self.length -= 1
             
         
    # method to delete a node after the node having the given data
    def deleteValue(self, data):
        
        currentnode = self.head
        previousnode = self.head
        count=0
        while currentnode.next != None:# or currentnode.data != data:
            
            if currentnode.data == data:
                
                if self.head.data==data:
                    self.head=previousnode.next = currentnode.next
                else:
                    previousnode.next = currentnode.next
                self.length -= 1
                return
                    
            else:
                previousnode = currentnode
                currentnode = currentnode.next
                
        if currentnode.next==None and currentnode.data==data:
            previousnode.next = currentnode.next
            self.length -= 1
        
                 
         
         
    # method to delete a node at a particular position
    def deleteAtPos(self, pos):
        count = 0
        currentnode = self.head
        previousnode = self.head
 
        if pos > self.length or pos < 0:
            print ("The position does not exist. Please enter a valid position")
        # to delete the first position of the linkedlist
        elif pos == 1:
            self.deleteBeg()
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


n=Node()
n.insertAtBeginning(4)

n.insertAtEnd(5)

n.insertAtEnd(7)
n.insertAtPos(1,99)
n.insertAtPos(2,900)
n.insertAtPos(3,1000)

n.listLength()

n.deleteValue(7)

print("\nAfter delete\n")

n.deleteAtPos(1)
n.deleteAtPos(3) 

n.listLength()


