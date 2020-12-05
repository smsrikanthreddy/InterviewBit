# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root):
        def recur(node):
            if not node:
                return
            recur(node.left)
            new_node[0].right = TreeNode(node.val)
            new_node[0] = new_node[0].right
            recur(node.right)

        head = TreeNode(0)
        new_node = [head]
        recur(root)
        return head.right


class Solution:
    def increasingBST(self, root):
        def recur(node):
            if not node: return
            recur(node.left)
            node.left = None  # clear left
            new_node[0].right = node  # reuse node
            new_node[0] = new_node[0].right
            recur(node.right)

        head = TreeNode(0)
        new_node = [head]
        recur(root)
        return head.right