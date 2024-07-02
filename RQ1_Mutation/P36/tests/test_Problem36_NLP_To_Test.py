import pytest
from Problem36_GeneratedSolution import lowestCommonAncestor as find_LCA, TreeNode  # Assuming the function 'find_LCA' and class 'TreeNode' are defined in 'solution.py'

# Helper function to create a binary tree from a list of values
def build_tree(values):
    if not values:
        return None
    iter_values = iter(values)
    root = TreeNode(next(iter_values))
    queue = [root]
    for val in iter_values:
        current = queue[0]
        if current.left is None:
            current.left = TreeNode(val) if val is not None else None
            if current.left:
                queue.append(current.left)
        else:
            current.right = TreeNode(val) if val is not None else None
            if current.right:
                queue.append(current.right)
            queue.pop(0)
    return root

# Helper function to find a node by value in a binary tree
def find_node(root, value):
    if root is None:
        return None
    if root.val == value:
        return root
    left = find_node(root.left, value)
    if left:
        return left
    return find_node(root.right, value)

@pytest.mark.parametrize("values, p_val, q_val, expected_val", [
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),  # Example 1
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),  # Example 2
    ([1, 2], 1, 2, 1),  # Example 3
    ([1], 1, 1, 1),  # Single node tree
    ([1, 2, 3, None, 4], 4, 3, 1),  # LCA at root with missing nodes
    ([5, 3, 6, 2, 4, None, 7], 2, 7, 5)  # LCA in a BST
])
def test_find_LCA(values, p_val, q_val, expected_val):
    """
    Tests the find_LCA function with various binary trees and node values to ensure it correctly identifies the lowest common ancestor.
    
    This test function ensures:
    - Proper construction of the binary tree from a list representation.
    - Accurate retrieval of the LCA, considering different tree shapes and node configurations.
    - Correct handling of edge cases, such as trees with a single node or missing child nodes.

    Args:
    values (list): List representation of the binary tree, where `None` represents a missing node.
    p_val (int): Value of the first node for which LCA is to be found.
    q_val (int): Value of the second node for which LCA is to be found.
    expected_val (int): The value of the expected LCA node.
    """
    root = build_tree(values)
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    lca = find_LCA(root, p, q)
    assert lca.val == expected_val, f"Test failed for values={values}, p_val={p_val}, q_val={q_val}. Expected LCA={expected_val}, found={lca.val if lca else 'None'}"

