class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    """
    Flatten the tree starting from the root following the pre-order traversal.
    """
    if not root:
        return
    
    # Flatten the left and right subtrees
    flatten(root.left)
    flatten(root.right)
    
    # Store the right subtree and attach the left subtree to the right
    temp_right = root.right
    root.right = root.left
    root.left = None  # Ensure the left child is set to None
    
    # Find the rightmost node of the current right subtree (originally left subtree)
    cur = root
    while cur.right:
        cur = cur.right
    
    # Attach the original right subtree to the rightmost node
    cur.right = temp_right

# Note: This solution modifies the tree in place and doesn't return anything.
