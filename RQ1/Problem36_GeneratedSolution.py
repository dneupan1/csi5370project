

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    """
    Find the lowest common ancestor (LCA) of two given nodes in the binary tree.
    
    :param root: TreeNode, the root of the binary tree.
    :param p: TreeNode, the first node.
    :param q: TreeNode, the second node.
    :return: TreeNode, the LCA of nodes p and q.
    """
    if not root or root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root  # If both left and right are non-null, root is the LCA
    return left if left else right  # Return the non-null child if any

