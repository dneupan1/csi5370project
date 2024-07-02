
import pytest
from Problem36_GeneratedSolution import lowestCommonAncestor, TreeNode 

def build_tree_and_map(values):
    if not values:
        return None, {}
    nodes = [None if val is None else TreeNode(val) for val in values]
    value_node_map = {val: node for val, node in zip(values, nodes) if val is not None}
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root, value_node_map

# Example usage
tree_values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root, nodes = build_tree_and_map(tree_values)

# Now, you can use `nodes` dictionary directly in your tests:
# nodes[5], nodes[6], etc., refer to TreeNode objects with those values

# Now, use root and nodes in your tests directly. Note that `root` is already correctly a TreeNode object.
# The assertion in the test functions should compare the values of the TreeNode objects, not the objects directly, 
# unless you are checking for the exact same instances.

# Updated test cases with proper assertion checks
def test_lca_left_subtree():
    p = nodes[5]
    q = nodes[6]
    assert lowestCommonAncestor(root, p, q).val == p.val, "Failed with both nodes in the left subtree"

def test_lca_different_subtrees():
    p = nodes[5]
    q = nodes[1]
    assert lowestCommonAncestor(root, p, q).val == nodes[3].val, "Failed with nodes in different subtrees"

def test_lca_right_subtree():
    p = nodes[0]
    q = nodes[8]
    assert lowestCommonAncestor(root, p, q).val == nodes[1].val, "Failed with both nodes in the right subtree"

def test_lca_with_root():
    p = nodes[3]
    q = nodes[4]
    assert lowestCommonAncestor(root, p, q).val == p.val, "Failed with the root being one of the nodes"

def test_lca_deeper_ancestor():
    p = nodes[7]
    q = nodes[4]
    assert lowestCommonAncestor(root, p, q).val == nodes[2].val, "Failed with a deeper common ancestor"

def test_lca_node_is_ancestor():
    p = nodes[5]
    q = nodes[2]
    assert lowestCommonAncestor(root, p, q).val == p.val, "Failed with one node being the ancestor of the other"
