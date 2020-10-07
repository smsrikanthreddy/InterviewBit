# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        value = TreeNode(val)
        if not root:
            return value
        prev1= root
        prev = prev1
        while root!=None:
                prev = root
                if value.val<root.val:
                    root = root.left
                else:
                    root = root.right
        if prev == None:
            prev = value
        if value.val< prev.val:
                prev.left = value
        else:
                prev.right = value
        del root, prev
        return prev1