#NODE DECLARATION
class BinaryTree:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
    #set data
    def setData(self, data):
        self.data = data
    #get data
    def getData(self):
        return self.data
    #get left child of a node
    def getLeft(self):
        return self.left
    #get right child of a node
    def getRight(self):
        return self.right

    def size(self):
            return self.size
            
    def isEmpty(self):
            return self.size == 0

# USING QUEUE 
class Queue:
    def __init__(self, limit=1000):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    def isEmpty(self):
        return self.size < 0
    def enQueue(self, item):
        if self.size >= self.limit:
            print ('Queue Overflow!')
            return
        else:
            self.que.append(item)
        if self.front is None:
            self.front = self.rear= 0
        else:
            self.rear = self.size
        self.size += 1
        return self.que
        
    def deQueue(self):
        if self.size>0:
            p=self.que.pop(0)
            self.size-=1
            if self.size == 0:
                self.front= self.rear =None
            else:
                self.rear = self.size-1
           # print(p.data)
            return p
           
  # Insert using level order traversal
def insertInBinaryTreeUsingLevelOrder(root, data):
    newNode = BinaryTree(data)
    if root is None:
        root = newNode
        return root
    q = Queue()
    q.enQueue(root)
    node = None
    while not q.isEmpty():
        node = q.deQueue()
        if data== node.getData():
             return root
        if node.left is not None:
            q.enQueue(node.left)
        else:
            node.left = newNode
            return root
        if node.right is not None:
            q.enQueue(node.right)
        else:
            node.right = newNode
            return root

 #PRINTING VALUES IN THE TREE-LEVEL ORDER TRAVERSAL.
def levelOrder (root):
    Q = Queue()
    
    if(root == None): 
            return None

    Q.enQueue(root)
    while(not Q.isEmpty()):
            temp = Q.deQueue()
            if temp is None:
                break
            print (temp.data)
            if(temp.left):
                    Q.enQueue(temp.left)
            if(temp.right): 
                    Q.enQueue(temp.right)

#CALLING FUNCTIONS AND INSERTING VALUES.   
root=BinaryTree(10)
root = insertInBinaryTreeUsingLevelOrder(root,11)

root = insertInBinaryTreeUsingLevelOrder(root,9)

root = insertInBinaryTreeUsingLevelOrder(root, 15)
root = insertInBinaryTreeUsingLevelOrder(root, 8)
root = insertInBinaryTreeUsingLevelOrder(root, 12)
root = insertInBinaryTreeUsingLevelOrder(root, 225)

levelOrder(root) #PRINTING VALUE






