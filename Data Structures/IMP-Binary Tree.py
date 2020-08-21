def findMaxUsingLevelOrder(root):
	if root is None:
		return

	q = Queue()
	q.enQueue(root)
	node = None
	maxElement = 0
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO

		if maxElement < node.get_data():
			maxElement = node.get_data()
		if node.left is not None:
			q.enQueue(node.left)

		if node.right is not None:
			q.enQueue(node.right)

	print (maxElement)

#---------------------------------------
def findUsingLevelOrder(root, data):
	if root is None:
		return -1

	q = Queue()
	q.enQueue(root)
	node = None
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO

		if data == node.get_data():
			return 1
		if node.left is not None:
			q.enQueue(node.left)
		if node.right is not None:
			q.enQueue(node.right)

	return 0

#_------------------------------------------

def findSizeusingLevelOrder(root):
	if root is None:
		return 0

	q = Queue()
	q.enQueue(root)
	node = None
	count = 0
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO
		count += 1
		if node.left is not None:
			q.enQueue(node.left)

		if node.right is not None:
			q.enQueue(node.right)

	return count

#----------------------------------------------------
def levelOrderTraversalInReverse(root):
    if root is None:
        return 0

    q = Queue()
    s = Stack()
    q.enQueue(root)
    node = None
    count = 0
    while not q.isEmpty():
        node = q.deQueue()  # dequeue FIFO
        if node.left is not None:
            q.enQueue(node.left)

        if node.right is not None:
            q.enQueue(node.right)
        s.push(node)

    while (not s.isEmpty()):
        print(s.pop().get_data())

#-----------------------------------------
#height of binarytree
def maxDepth(root):
	if root == None:
	    return 0
	return max(maxDepth(root.getLeft()), maxDepth(root.getRight())) + 1
#non recurrsive method
def maxDepth(self, root):
	if root == None:
	    return 0
	q = []
	q.append([root, 1])
	temp = 0
	while len(q) != 0:
	    node, depth = q.pop()
	    depth = max(temp, dep)
	    if node.getLeft() != None:
		q.append([node.getLeft(), depth + 1])
	    if node.getRight() != None:
		q.append([node.getRight(), depth + 1])
	return temp

#---------------------------------------------------
def deepestNode(root):
	if root is None:
		return 0
	q = Queue()
	q.enQueue(root)
	node = None
	count = 0
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO
		if node.left is not None:
			q.enQueue(node.left)

		if node.right is not None:
			q.enQueue(node.right)
	return node.get_data()

#-----------------------------------------------
def numberOfLeavesInBTusingLevelOrder(root):
	if root is None:
		return 0
	q = Queue()
	q.enQueue(root)
	node = None
	count = 0
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO
		if node.left is None and node.right is None:
			count += 1
		else:
			if node.left is not None:
				q.enQueue(node.left)

			if node.right is not None:
				q.enQueue(node.right)
	return count

#------------------------------------------------

def numberOfFullNodesInBTusingLevelOrder(root):
	if root is None:
		return 0
	q = Queue()
	q.enQueue(root)
	node = None
	count = 0
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO
		if node.left is not None and node.right is not None:
			count += 1
		if node.left is not None:
			q.enQueue(node.left)

		if node.right is not None:
			q.enQueue(node.right)
	return count

#_----------------------------------------------------
def numberOfHalfNodesInBTusingLevelOrder(root):
	if root is None:
		return 0
	q = Queue()
	q.enQueue(root)
	node = None
	count = 0
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO
		if (node.left is None and node.right is not None) or \
			(node.left is not None and node.right is None):
			count += 1
		if node.left is not None:
			q.enQueue(node.left)

		if node.right is not None:
			q.enQueue(node.right)
	return count

#-------------------------------------------
def areStructurullySameTrees(root1, root2):
	if (not root1.left) and not (root1.right) and (not root2.left) and \
		not (root2.right) and root1.data == root2.data:
		return True

	if (root1.data != root2.data) or (root1.left and not root2.left) or \
		(not root1.left and root2.left) or (root1.right and not root2.right) \
		or (not root1.right and root2.right):
		return False

	left = areStructurullySameTrees(root1.left, root2.left) if root1.left and root2.left else True
	right = areStructurullySameTrees(root1.right, root2.right) if root1.right and root2.right else True
	return left and right

#-------------------------------------------------------
#to find diameter of tree
def findMaxLen(root):
    nMaxLen = 0
    if (root == None):
        return 0
    if (root.left == None):
        root.nMaxLeft = 0
    if (root.right == None):
        root.nMaxRight = 0
    if (root.left != None):
        findMaxLen(root.left)
    if (root.right != None):
        findMaxLen(root.right)
    if (root.left != None):
        nTempMaxLen = 0
        nTempMaxLen = max(root.left.nMaxLeft, root.left.nMaxRight)
        root.nMaxLeft = nTempMaxLen + 1

    if (root.right != None):
        nTempMaxLen = 0
        nTempMaxLen = max(root.right.nMaxLeft, root.right.nMaxRight)
        root.nMaxRight = nTempMaxLen + 1

    if (root.nMaxLeft + root.nMaxRight > nMaxLen):
        nMaxLen = root.nMaxLeft + root.nMaxRight
    return nMaxLen
#-----------------------------------------------------------------------------
def findLevelwithMaxSum(root):
    if root is None:
        return 0
    q = Queue()
    q.enQueue(root)
    q.enQueue(None)
    node = None
    level = maxLevel = currentSum = maxSum = 0
    while not q.isEmpty():
        node = q.deQueue()  # dequeue FIFO
        # If the current level is completed then compare sums
        if (node == None):
            if (currentSum > maxSum):
                maxSum = currentSum
                maxLevel = level

            currentSum = 0
            # place the indicator for end of next level at the end of queue
            if not q.isEmpty():
                q.enQueue(None)
                level += 1
        else:
            currentSum += node.get_data()
            if node.left is not None:
                q.enQueue(node.left)

            if node.right is not None:
                q.enQueue(node.right)
    return maxLevel
#------------------------------------------------------------
def pathsAppender(root, path, paths):
    if not root:
        return 0

    path.append(root.data)
    paths.append(path)
    pathsAppender(root.left, path + [root.data], paths)
    pathsAppender(root.right, path + [root.data], paths)  # make sure it can be executed!


def pathsFinder(root):
    paths = []
    pathsAppender(root, [], paths)
    print('paths:', paths)

#--------------------------------------------------------
def treeMaximumSumPath(node, is_left=True, Lpath={}, Rpath={}):
    if is_left:
        # left sub-tree
        if not node.left:
            Lpath[node.id] = 0
            return 0
        else:
            Lpath[node.id] = node.data + max(
                treeMaximumSumPath(node.left, True, Lpath, Rpath),
                treeMaximumSumPath(node.left, False, Lpath, Rpath)
            )
            return Lpath[node.id]
    else:
        # right sub-tree
        if not node.right:
            Rpath[node.id] = 0
            return 0
        else:
            Rpath[node.id] = node.data + max(
                treeMaximumSumPath(node.right, True, Lpath, Rpath),
                treeMaximumSumPath(node.right, False, Lpath, Rpath)
            )
            return Rpath[node.id]


def maxsum_path(root):
    Lpath = {}
    Rpath = {}
    treeMaximumSumPath(root, True, Lpath, Rpath)
    treeMaximumSumPath(root, False, Lpath, Rpath)
    print 'Left-path:', Lpath
    print 'Right-path:', Rpath
    path2sum = dict((i, Lpath[i] + Rpath[i]) for i in Lpath.keys())
    i = max(path2sum, key=path2sum.get)
    print 'The path going through node', i, 'with max sum', path2sum[i]
    return path2sum[i]

#=----------------------------------------
#problem 23
def pathFinder(root, val, path, paths):
    if not root:
        return False

    if not root.left and not root.right:
        if root.data == val:
            path.append(root.data)
            paths.append(path)
            return True
        else:
            return False

    left = pathFinder(root.left, val - root.data, path + [root.data], paths)
    right = pathFinder(root.right, val - root.data, path + [root.data], paths)  # make sure it can be executed!
    return left or right


def hasPathWithSum(root, val):
    paths = []
    pathFinder(root, val, [], paths)
    print('sum:', val)
    print('paths:', paths)

########-----------------------------------------------
#problem 25
def sumInBinaryTreeLevelOrder(root):
	if root is None:
		return 0
	q = Queue()
	q.enQueue(root)
	node = None
	sum = 0
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO
		sum += node.get_data()
		if node.left is not None:
			q.enQueue(node.left)

		if node.right is not None:
			q.enQueue(node.right)
	return sum

#----------------------------------------
def AreMirrors(root1, root2):
	if(root1 == None and root2 == None):
		return 1
	if(root1 == None or root2 == None):
		return 0
	if(root1.data != root2.data):
		return 0
	else:
		return AreMirrors(root1.left, root2.right) and AreMirrors(root1.right, root2.left)

#--------------------------------------
#least common ancestors # problem 28
def FindLCA(root, a, b):
	while(root):
		if((a <= root.data and b > root.data) or (a > root.data and b <= root.data)):
			return root
		if(a < root.data):
			root = root.left
		else: root = root.right

#----------------------------------------------------
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None  # inorder is empty
            root = TreeNode(preorder[0])
            rootPos = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1: 1 + rootPos], inorder[: rootPos])
            root.right = self.buildTree(preorder[rootPos + 1:], inorder[rootPos + 1:])
        return root

#ALTERNATIVE SOLUTION
class Solution2:
    def buildTree(self, preorder, inorder):
        return self.buildTreeRec(preorder, inorder, 0, 0, len(preorder))

    def buildTreeRec(self, preorder, inorder, indPre, indIn, element):
        if element == 0:
            return None
        solution = TreeNode(preorder[indPre])
        numElementsLeftSubtree = 0;
        for i in range(indIn, indIn + element):
            if inorder[i] == preorder[indPre]:
                break
            numElementsLeftSubtree += 1
        solution.left = self.buildTreeRec(preorder, inorder, indPre + 1, indIn, numElementsLeftSubtree)
        solution.right = self.buildTreeRec(preorder, inorder, indPre + numElementsLeftSubtree + 1,
                                           indIn + numElementsLeftSubtree + 1, element - 1 - numElementsLeftSubtree)
        return solution

#--------------------------------------------------------------
def PrintAllAncestors(root, node):
	if(root == NULL):
		return 0
	if(root.left == node or root.right == node or  PrintAllAncestors(root.left, node) or PrintAllAncestors(root.right, node)):
		print(root.data)
		return 1
	return 0
#-----------------------------------------

#SPIRAL ORDER TRAVERSAL OR ZIG ZAG
def zigzagLevelOrder(self, root):
	result = []
	currentLevel = []
	if root != None:
	    currentLevel.append(root)
	leftToRight = True
	while len(currentLevel) > 0:
	    levelresult = []
	    nextLevel = []
	    while len(currentLevel) > 0:
		node = currentLevel.pop()
		levelresult.append(node.val)
		if leftToRight:
		    if node.left != None:
			nextLevel.append(node.left)
		    if node.right != None:
			nextLevel.append(node.right)
		else:
		    if node.right != None:
			nextLevel.append(node.right)
		    if node.left != None:
			nextLevel.append(node.left)
	    currentLevel = nextLevel
	    result.append(levelresult)
	    leftToRight = not leftToRight
	return result
#-----------------------------------------------
def fillNextSiblingsWithLevelOrderTraversal(root):
	if root is None:
		return 0

	q = Queue()
	q.enQueue(root)
	node = None
	count = 0
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO
		node.nextSibling = q.queueFront()
		if node.left is not None:
			q.enQueue(node.left)

		if node.right is not None:
			q.enQueue(node.right)

#--------------------------------------------
#TO COMPUTE MIRROR.
def MirrorOfBinaryTree(root):
    if (root != None):
        MirrorOfBinaryTree(root.left)
        MirrorOfBinaryTree(root.right)

        # swap the pointers in this node
        temp = root.left
        root.left = root.right
        root.right = temp

    return root
