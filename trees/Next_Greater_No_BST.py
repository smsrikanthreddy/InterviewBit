# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree

    def find_node(self, root, data):
        if root is None:
            return None
        while root:
            if root.val > data:
                root = root.left
            elif root.val < data:
                root = root.right
            else:
                return root

    def find_min(self, root):
        if root is None:
            return None
        while root.left:
            root = root.left
        return root

    def getSuccessor(self, A, B):
        current = self.find_node(A, B)
        if current.val is None:
            return None
        if current.right is not None:
            return self.find_min(current.right)
        else:
            ancestor = A
            successor = None
            while (ancestor != current):
                if current.val < ancestor.val:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor