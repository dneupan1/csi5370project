class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a TreeNode with a value, left child, and right child.
        :param val: Integer value of the node.
        :param left: TreeNode representing the left child.
        :param right: TreeNode representing the right child.
        """
        self.val = val
        self.left = left
        self.right = right

def flatten(root: TreeNode) -> None:
    """
    Flattens a binary tree into a linked list in-place using the same TreeNode class. 
    The linked list follows the pre-order traversal order, with all left children set to None.
    
    :param root: TreeNode, the root of the binary tree.
    """
    # Start with the current node set to the root
    current = root
    while current:
        if current.left:
            # Find the rightmost node of the left subtree
            rightmost = current.left
            while rightmost.right:
                rightmost = rightmost.right
            # Connect the rightmost node of the left subtree to the right child of the current node
            rightmost.right = current.right
            # Move the left subtree to the right
            current.right = current.left
            current.left = None
        # Move to the next node on the right (originally the left child)
        current = current.right

def list_to_tree(data):
    """
    Converts a list into a binary tree using level order insertion.

    :param data: List of integers where None represents a missing node.
    :return: TreeNode, the root of the binary tree.
    """
    if not data:
        return None
    it = iter(data)
    root = TreeNode(next(it))
    queue = [root]
    for val in it:
        node = queue.pop(0)
        if val is not None:
            node.left = TreeNode(val)
            queue.append(node.left)
        if next(it, None) is not None:
            node.right = TreeNode(next(it))
            queue.append(node.right)
    return root

def tree_to_list(root):
    """
    Converts a flattened binary tree to a list representing the linked list.

    :param root: TreeNode, the root of the flattened binary tree.
    :return: List of values in the linked list format.
    """
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result
