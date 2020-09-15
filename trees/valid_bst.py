'''
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer

    def isValidBST(self, A):

        def check_bst(root):
            if root.left is not None and root.left.val > root.val:
                return 0
            elif root.right is not None and root.right.val < root.val:
                return 0
            else:
                check_bst(root.left)
                check_bst(root.right)
                return 1

        if A is None:
            return 0
        else:
            return check_bst(A)
'''


# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        def inOrder_Traversal(root, prev):
            if root != None:
                if inOrder_Traversal(root.left, prev)== True:
                    return 0
                if prev != None and root.val <= prev.val:
                    return 0
                prev = root
                inOrder_Traversal(root.right, prev)
            return 1
        #import pdb; pdb.set_trace()
        prev = None
        return inOrder_Traversal(A, prev)


# Driver Code
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(40)
    sol = Solution()
    print(sol.isValidBST(root))
    #if (isBST(root) == None):