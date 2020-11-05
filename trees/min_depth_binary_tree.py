# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, root):
        # Null node has 0 depth.
        if root == None:
            return 0

        # Leaf node reached.
        if root.left == None and root.right == None:
            return 1

        # Current node has only right subtree.
        if not root.left:
            return 1 + self.minDepth(root.right)

        # Current node has only left subtree.
        elif not root.right:
            return 1 + self.minDepth(root.left)

        # if none of the above cases, then recur on both left and right subtrees.
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))