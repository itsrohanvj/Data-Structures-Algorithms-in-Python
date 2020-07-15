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

#FINDING THE VALUE
def find(root, data):
    currentNode = root
    while currentNode:
        if data== currentNode.data:
            return currentNode.data
        if data < currentNode.data:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
    return None

#INSERTING VALUES
r = Node(50)
insertNode(r, Node(30))
insertNode(r, Node(20))
insertNode(r, Node(40))
insertNode(r, Node(70))
insertNode(r, Node(60))
insertNode(r, Node(80))

output=find(r,20)
print("Found=",output)
