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

def pathSum(root: TreeNode, targetSum: int) -> int:
    """
    Returns the number of paths that sum to a target value in a binary tree.
    Paths must go downwards from parent to child nodes.

    :param root: TreeNode, the root of the binary tree.
    :param targetSum: Integer, the target sum to find in paths.
    :return: Integer, number of paths that sum to targetSum.
    """
    # Dictionary to store the current path sum frequency
    prefix_sum_count = {}
    prefix_sum_count[0] = 1  # To handle the case where path sum equals targetSum directly

    def dfs(node, current_sum):
        if not node:
            return 0
        
        # Current path sum including the current node
        current_sum += node.val
        # Paths ending at the current node that sum to targetSum
        path_count = prefix_sum_count.get(current_sum - targetSum, 0)
        
        # Update the path sum count
        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
        
        # Recursively search in left and right subtrees
        path_count += dfs(node.left, current_sum)
        path_count += dfs(node.right, current_sum)
        
        # Revert the current node's value from the path sum count before returning to parent
        prefix_sum_count[current_sum] -= 1
        
        return path_count

    return dfs(root, 0)

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