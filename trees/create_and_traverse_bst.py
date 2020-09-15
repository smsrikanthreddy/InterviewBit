class Node:
    # Constructor to create a Binary Tree node
    def __init__(self, value ,left=None ,right=None):
        self.data = value
        self.left = left
        self.right = right


# Insert node in BSTsrmet
def insert(root: Node, data: int):
    if root is None:
        root = Node(data)
    elif data <= root.data:
        # insert to left
        root.left = insert(root.left, data)
    else:
        # insert to right
        root.right = insert(root.right, data)
    return root

def inorder_print(root: Node):
    if root is None: return
    inorder_print(root.left)
    print(root.data)
    inorder_print(root.right)


if __name__ == "__main__":
    # Driver program

    '''
    Ex 1: (edit above to get this tree if needed, as in https://gist.github.com/mycodeschool/6515e1ec66482faf9d79
       5
      / \
     3   10
    / \    \ 
   1   4   11

   Ex 2: demo below

       6
      / \
     3   10
    / \    \ 
   1   4   11
        \
         5

    To find the predecessor (as opposed to the successor), we simply have 2 cases as above:
        Case 1. There is a left subtree (e.g. take "6" above), so the predecessor is the max of that
        Case 2. No left subtree, so we get the closest ancestor where the current node is on the right
        [Note: I haven't implemented it in this code]
    '''
    root = Node(6)
    root = insert(root, 10)
    root = insert(root, 3)
    root = insert(root, 4)
    root = insert(root, 1)
    root = insert(root, 11)
    root = insert(root, 5)

    inorder_print(root)