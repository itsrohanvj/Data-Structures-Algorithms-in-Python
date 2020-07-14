class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insertNode(root, node):
   # print("node=",node.data, root.data)
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insertNode(root.right, node)

def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print (root.data)
    inOrderTraversal(root.right)

def preOrderTraversal(root):
    if not root:
        return        
    print (root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


def levelOrder (root):
    q=[]
    if(root == None): 
            return None
    q.append(root)
    while(len(q)>0):
            temp = q.pop(0)
            if temp is None:
                break
            print (temp.data)
            if(temp.left):
                    q.append(temp.left)
            if(temp.right): 
                    q.append(temp.right)

def postOrderRecursive(root):
    if not root:
        return
    
    postOrderRecursive(root.left)
    postOrderRecursive(root.right)
    print(root.data)

r = Node(50)
insertNode(r, Node(30))
insertNode(r, Node(20))
insertNode(r, Node(40))
insertNode(r, Node(70))

print ("in order:")
inOrderTraversal(r)

print("level Order")
levelOrder(r)

print ("pre order")
preOrderTraversal(r)

print("post oder")
postOrderRecursive(r)
