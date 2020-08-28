# Returns true if a binary tree is a binary search tree
def IsBST3(root):
    if root == None:
        return 1

    # false if the max of the left is > than root
    if (root.getLeft() != None and FindMax(root.getLeft()) > root.get_data())
        return 0

    # false if the min of the right is <= than root
    if (root.getRight() != None and FindMin(root.getRight()) < root.get_data())
        return 0

    # false if, recursively, the left or right is not a BST
    if (not IsBST3(root.getLeft()) or not IsBST3(root.getRight()))
        return 0

    # passing all that, it's a BST
    return 1

#METHOD 2
def isBST4(root, previousValue=[NEG_INFINITY]):
    if root is None:
        return 1
    if not isBST4(root.getLeft(), previousValue):
        return False
    if root.get_data() < lastNode[0]:
        return 0
    previousValue = root.get_data()
    return isBST4(root.getRight(), previousValue)

#-----------------------------------------------------------------------
def DLLtoBalancedBST(head):
	if(not head or not head.next):
		return head
	temp = FindMiddleNode(head)  # Refer Linked Lists chapter for this function.
	p = head   #We can use two-pointer logic to find the middle node
	while(p.next != temp):
		p = p.next
	p.next = None
	q = temp.next
	temp.next = None
	temp.prev = DLLtoBalancedBST(head)
	temp.next = DLLtoBalancedBST(q)
	return temp
#----------------------------------------------------------
def  BuildBST(A, left, right) :
	if(left > right):
		return None
	newNode = Node()
	if(not newNode) :
		print("Memory Error")
		return

	if(left == right):
		newNode.data = A[left]
		newNode.left = None
		newNode.right = None
	else :
		mid = left + (right - left) / 2
		newNode.data = A[mid]
		newNode.left = BuildBST(A, left, mid - 1)
		newNode.right = BuildBST(A, mid + 1, right)
	return newNode

if __name__ == "__main__":
	# create the sample BST
	A = [2, 3, 4, 5, 6, 7]
	root = BuildBST(A, 0, len(A) - 1)
	print "\ncreating BST"
	printBST(root)
#-------------------------------------------------------
count = 0


def kthSmallestInBST(root, k):
    global count
    if (not root):
        return None
    left = kthSmallestInBST(root.left, k)
    if (left):
        return left
    count += 1
    if (count == k):
        return root
    return kthSmallestInBST(root.right, k)
#-------------------------------------------------------
def SortedListToBST(ll, start, end):
	if(start > end):
		return None
	# same as (start+end)/2, avoids overflow
	mid = start + (end - start) // 2
	left = SortedListToBST(ll, start, mid - 1)
	root = BSTNode(ll.head.data)
	ll.deleteBeg()
	root.left = left
	root.right = SortedListToBST(ll, mid + 1, end)
	return root

def convertSortedListToBST(ll, n) :
	return SortedListToBST(ll, 0, n - 1)

#------------------------------------------------------
#PROBLEM 96 : narasimha
class Answer:
    def maxPathSum(self, root):
        self.maxValue = float("-inf")
        self.maxPathSumRec(root)
        return self.maxValue

    def maxPathSumRec(self, root):
        if root == None:
            return 0
        leftSum = self.maxPathSumRec(root.left)
        rightSum = self.maxPathSumRec(root.right)
        if leftSum < 0 and rightSum < 0:
            self.maxValue = max(self.maxValue, root.val)
            return root.val
        if leftSum > 0 and rightSum > 0:
            self.maxValue = max(self.maxValue, root.val + leftSum + rightSum)
        maxValueUp = max(leftSum, rightSum) + root.val
        self.maxValue = max(self.maxValue, maxValueUp)
        return maxValueUp
