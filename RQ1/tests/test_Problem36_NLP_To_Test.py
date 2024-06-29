class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    """
    Finds the lowest common ancestor (LCA) of two given nodes in the binary tree.
    
    Args:
    root (TreeNode): The root of the binary tree.
    p (TreeNode): The first node.
    q (TreeNode): The second node.
    
    Returns:
    TreeNode: The LCA of nodes p and q.
    """
    # Base case: if the tree is empty or if we find either p or q
    if root is None or root == p or root == q:
        return root
    
    # Recur for left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    # If both left and right are non-null, p and q are found in different subtrees
    if left and right:
        return root
    
    # Otherwise, check if left subtree or right subtree is LCA
    return left if left else right

# Helper function to build the tree from a list (BFS)
def build_tree(nodes):
    """
    Builds a binary tree from a list using BFS.
    
    Args:
    nodes (List[Optional[int]]): List of values to build the tree from.
    
    Returns:
    TreeNode: The root of the binary tree.
    """
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    
    return root
