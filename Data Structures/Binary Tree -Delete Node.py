# NORMAL BINARY TREE DELETE OPERATION AND INSERTION U SING LEVEL ORDER TRAVERSAL.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Inorder traversal of a binary tree
def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

# LEVEL ORDER TRAVERSAL
def levelOrder(root):
    q=[]

    if (root == None):
        return None

    q.append(root)
    while (not len(q)<1):
        temp = q.pop(0)
        if temp is None:
            break
        print(temp.data, end=" ")
        if (temp.left):
            q.append(temp.left)

        if (temp.right):
            q.append(temp.right)

# function to delete the given deepest node (d_node) in binary tree
def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

# function to delete element in binary tree
def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    print("len=",len(q))
    while (len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        deleteDeepest(root, temp)
        key_node.data = x
    return root

#FUNCTION TO INSERT NODE USING LEVEL ORDER. IT IS A NORMAL BINARY TREE AND NOT BINRARY SEARCH TREE.
def insertNode(root, data):
    newNode = Node(data)
    if root is None:
        root = newNode
        return root
    q = []
    q.append(root)
    node = None
    while not len(q)<1:
        node = q.pop(0)
        if data== node.data:  
             return root
        if node.left is not None:
            q.append(node.left)
        else:
            node.left = newNode
            return root
        if node.right is not None:
            q.append(node.right)
        else:
            node.right = newNode
            return root



# CALLING FUNCTIONS.
if __name__ == '__main__':

    root = Node(3)
    root=insertNode(root,2)
    root=insertNode(root,8)
    root=insertNode(root,5)
    root=insertNode(root,1)
    root=insertNode(root,7)
    root=insertNode(root,6)

    print("\n The tree before the deletion (printing inorder):")
    inorder(root)
    print("\n LEVEL ORDER \n")
    levelOrder(root)

    key = 2 # value to be deleted from tree
    root = deletion(root, key)

    print("\nThe tree after the deletion(printing inorder):")
    inorder(root)
    print("\nLevel order after deletion\n")
    levelOrder(root)