def sortedArrayToBST(self, A):
    if not A: return None
    mid = int(len(A) / 2)
    root = TreeNode(A[mid])
    root.left = self.sortedArrayToBST(A[:mid])
    root.right = self.sortedArrayToBST(A[mid + 1:])
    return root