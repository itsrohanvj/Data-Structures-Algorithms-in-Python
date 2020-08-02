class Node:
    # If data is not given by user,ils taken as None
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next= next
        self.prev = prev
        self.head= None
        self.tail=None
        self.length=0
    #method for setting Lhe data field or I.he node
    def setData(self,data):
        self.data =data
    #method for getting the data field of the node
    def getData(self):
        return self.data
    #method for setting the next fie ld of the node
    def setNext(self,next):
        self.next= next
    #method for getting the next field of the node
    def getNext(self):
        return self.next
    #returns true if the node points to another node
    def hasNext(self):
        return self.next != None
    #method ror setting the next field of the node
    def setPrev(self,prev):
        self.prev = prev
    #method for getting the next field of the node
    def getPrev(self):
        return self.prev
    #returns true if the node points to another node
    def hasPrev(self):
        return self.prev != None
    # str returns string equivalent of Object
    def __str__(self):
        return "Node[Data = %s}" % (self.data,)


    def insertAtBeginning(self, data):
        newNode = Node(data, None, None)
        if (self.head == None): #To imply that if head ==None
            self.head = self.tail = newNode
        else:
            newNode.setPrev(None)
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
        self.length+=1
        
    def insertAtEnd(self,data):
        if (self.head == None): #To imply that if head ... None
            self.head == Node(data)
            self.tail=self.head
        else:
            current = self.head
            while(current.getNext() != None):
                current =current.getNext()
            current.setNext(Node(data, None, current))
            self.tail = current.getNext()
        self.length+=1
        
        # PRINTING VALUES OF LIST
    def listLength(self):         
        current = self.head
        count=0
        while  current!=None:
            count=count+1
            print(current.getData())
            current = current.getNext()
        print("count=",count)
    def getNode(self, index):
        currentNode = self.head
        if currentNode == None:
            return None
        i = 1
        while i < index and currentNode.getNext() is not None:
            currentNode =currentNode.getNext()
            if currentNode == None:
                break
            i += 1
        return currentNode
    
    
    def insertAtGivenPosition(self, index, data):
        if index > self.length or index < 1:
            return None
        else:
            newNode = Node(data)
            if self.head == None or index == 1:
                self.insertAtBeginning(data)
            elif index > 0:
                temp = self.getNode(index) #calls the above function to find node.
                if temp == None or temp.getNext() == None:
                    self.insertAtEnd(data)
                else:
                    newNode.setNext(temp.getNext())
                    newNode.setPrev(temp)
                    temp.getNext().setPrev(newNode)
                    temp.setNext(newNode)
        self.length+=1

    def deleteBeg(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            self.head.setPrev(None)
            self.length -= 1

    # method to delete the last node of the linked list
    def deleteLast(self):

        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head

            while currentnode.next != None:
                previousnode = currentnode
                currentnode = currentnode.next
            self.tail=previousnode
            previousnode.next = None

            self.length -= 1
#at position
    def gettNode(self, index):
        if index>self.length or index<1:
            return
        else:
            currentNode = self.head
            if currentNode == None:
                return None
            i=1
            while i < index:
                currentNode = currentNode.getNext()
                if currentNode == None:
                    break
                i += 1
            return currentNode

    def deleteAtGivenPosition(self, index):
        temp = self.gettNode(index)
        if temp :
            if temp ==self.head:
                self.deleteBeg()
            elif temp==self.tail:
                self.deleteLast()
            else:
                temp.getPrev().setNext(temp.getNext())
                if temp.getNext():
                
                    temp.getNext().setPrev(temp.getPrev())
            temp.setPrev(None)
            temp.setNext(None)
            temp.setData(None)
            
        #Deleting with given data
    def deleteWithData(self, data):
        temp = self.head
        
        while temp.getNext() is not None:
            if temp.getData() == data:
                # if it's not the first clement
                if temp.getNext() is not None and temp.getPrev() is not None:
                    temp.getPrev().setNext(temp.getNext())
                    temp.getNext().setPrev(temp.getPrev())
                else:
                    #otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = temp.getNext()
                    temp.getNext().setPrev(None)

            temp = temp.getNext()
        if temp.getNext() is None and data==self.tail.data:
            temp.getPrev().setNext(None)
           
	        
 #CALLING FUNCTIONS  
n=Node()

n.insertAtGivenPosition(100,55995)
n.insertAtBeginning(4)
n.insertAtEnd(5)
n.insertAtEnd(7)
n.insertAtBeginning(99)
n.insertAtGivenPosition(1,555)

n.listLength()

print("\nAfter Delete\n")
n.deleteAtGivenPosition(3)
n.deleteWithData(5)
n.listLength()




