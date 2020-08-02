class BinaryTree:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
        
# Insert using level order traversal and printing

def LevelOrder(root, data):
    newNode = BinaryTree(data)
    if root is None:
        root = newNode
        print(root.data)
        return root
    q = []  #QUEUE
    q.append(root)
    node = None
    
    while  len(q)>0:
        node=q.pop(0)
        if data== node.data:
            return root
        if node.left is not None:
            q.append(node.left)
        else:
            node.left = newNode
            q.append(node.left)
            print(node.left.data)
            return root
        
        if node.right is not None:
            q.append(node.right)
        else:
            node.right = newNode
            q.append(node.right)
            print(node.right.data)
            return root
        
#calling functions
root=LevelOrder(None,10)
root = LevelOrder(root,11)
root = LevelOrder(root,9)
root = LevelOrder(root, 15)
root = LevelOrder(root, 8)
root = LevelOrder(root, 12)
root = LevelOrder(root, 225)







