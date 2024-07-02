import pytest

# Assuming the function 'pathSum' is defined in 'solution.py'
from Problem13_GeneratedSolution import pathSum, TreeNode

def build_tree(values):
    """
    Helper function to build a binary tree from a list of values.
    """
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [(root, 0)]
    while queue:
        node, i = queue.pop(0)
        left_i, right_i = 2 * i + 1, 2 * i + 2
        if left_i < len(values) and values[left_i] is not None:
            node.left = TreeNode(values[left_i])
            queue.append((node.left, left_i))
        if right_i < len(values) and values[right_i] is not None:
            node.right = TreeNode(values[right_i])
            queue.append((node.right, right_i))
    return root

@pytest.mark.parametrize("values, targetSum, expected", [
    # Example 1: Provided in the problem description
    ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
    # Example 2: Provided in the problem description
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3),
    # Edge case: Single node tree where node value equals targetSum
    ([5], 5, 1),
    # Edge case: Single node tree where node value does not equal targetSum
    ([5], 1, 0),
    # Multiple paths with the same sum
    ([1, 2, 3, 4, 5, 6, 7], 10, 2),  # Paths: [1, 2, 7] and [3, 7]
    # All nodes with the same value
    ([1, 1, 1, 1, 1], 2, 4),  # Multiple paths that sum to 2
    # Complex tree with multiple paths summing to target
    ([1, -2, -3, 1, 3, -2, None, -1], -1, 4),  # Paths: [-2, 1], [1, -2], [1, -3], [-2, 1, -1]
    # Tree with no paths summing to target
    ([1, 2, 3], 100, 0)
])
def test_pathSum(values, targetSum, expected):
    """
    Tests the pathSum function with various binary tree structures and target sums to ensure it correctly counts the number of paths that sum to targetSum.

    This test function verifies:
    - Proper handling of various tree structures, including edge cases.
    - Correct counting of paths that sum to targetSum.
    - Accurate handling of trees with multiple paths and different values.

    Args:
    values (list of int or None): The list of values representing the binary tree in level-order.
    targetSum (int): The target sum to find paths for.
    expected (int): The expected number of paths that sum to targetSum.
    """
    root = build_tree(values)
    result = pathSum(root, targetSum)
    assert result == expected, f"Test failed for values={values}, targetSum={targetSum}. Expected {expected}, got {result}"
