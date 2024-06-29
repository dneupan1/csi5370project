import pytest
from Problem12_GeneratedSolution import flatten, TreeNode  # Adjust the import path as needed

def build_tree_from_list(values):
    """
    Helper function to build a binary tree from a list.
    """
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    index = 1
    while index < len(values):
        node = queue.pop(0)
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root

def tree_to_list(root):
    """
    Helper function to convert a flattened tree to a list.
    """
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result

def test_flatten_empty_tree():
    """
    Test flattening an empty tree.
    """
    root = build_tree_from_list([])
    flatten(root)
    assert tree_to_list(root) == [], "Empty tree should remain unchanged"

def test_flatten_single_node():
    """
    Test flattening a tree with a single node.
    """
    root = build_tree_from_list([1])
    flatten(root)
    assert tree_to_list(root) == [1], "Single node tree should remain unchanged"

def test_flatten_complex_tree():
    """
    Test flattening a more complex tree.
    """
    root = build_tree_from_list([1, 2, 5, 3, 4, None, 6])
    flatten(root)
    expected = [1, 2, 3, 4, 5, 6]
    assert tree_to_list(root) == expected, "Complex tree was not flattened correctly"

def test_flatten_right_heavy_tree():
    """
    Test flattening a right-heavy tree.
    """
    root = build_tree_from_list([1, None, 2, None, 3, None, 4])
    flatten(root)
    expected = [1, 2, 3, 4]
    assert tree_to_list(root) == expected, "Right-heavy tree was not flattened correctly"
