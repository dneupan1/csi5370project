# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Problem36_GeneratedSolution as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 619
    var_0 = module_0.lowestCommonAncestor(int_0, int_0, int_0)
    assert var_0 == 619
    bool_0 = True
    float_0 = 206.3468
    module_0.lowestCommonAncestor(bool_0, float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "k@Pg_(c^?i_S`"
    none_type_0 = None
    var_0 = module_0.lowestCommonAncestor(none_type_0, str_0, none_type_0)
    module_0.lowestCommonAncestor(str_0, var_0, none_type_0)


def test_case_2():
    int_0 = 4290
    tree_node_0 = module_0.TreeNode(int_0)


def test_case_3():
    int_0 = -2148
    none_type_0 = None
    var_0 = module_0.lowestCommonAncestor(int_0, none_type_0, int_0)
    assert var_0 == -2148
    tree_node_0 = module_0.TreeNode(right=var_0)
    assert tree_node_0.val == 0
    var_1 = module_0.lowestCommonAncestor(tree_node_0, tree_node_0, none_type_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "Problem36_GeneratedSolution.TreeNode"
    )
    assert var_1.val == 0
    assert var_1.left is None
    assert var_1.right == -2148
    list_0 = []
    tree_node_1 = module_0.TreeNode(right=list_0)
    assert tree_node_1.val == 0
    tree_node_2 = module_0.TreeNode(none_type_0, right=none_type_0)


def test_case_4():
    tree_node_0 = module_0.TreeNode()
    assert tree_node_0.val == 0
    tree_node_1 = module_0.TreeNode()
    assert tree_node_1.val == 0
    var_0 = module_0.lowestCommonAncestor(tree_node_0, tree_node_0, tree_node_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "Problem36_GeneratedSolution.TreeNode"
    )
    assert var_0.val == 0
    assert var_0.left is None
    assert var_0.right is None
    tree_node_2 = module_0.TreeNode(right=tree_node_1)
    assert tree_node_2.val == 0
    var_1 = module_0.lowestCommonAncestor(var_0, tree_node_2, tree_node_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "Problem36_GeneratedSolution.TreeNode"
    )
    assert var_1.val == 0
    assert var_1.left is None
    assert var_1.right is None
    none_type_0 = None
    tree_node_3 = module_0.TreeNode(left=tree_node_0, right=none_type_0)
    assert tree_node_3.val == 0
    var_2 = module_0.lowestCommonAncestor(tree_node_3, tree_node_2, var_0)
    assert var_2.val == 0
    assert var_2.left is None
    tree_node_4 = module_0.TreeNode()
    assert tree_node_4.val == 0
    var_3 = module_0.lowestCommonAncestor(tree_node_1, tree_node_3, tree_node_3)


def test_case_5():
    float_0 = 1997.0153
    none_type_0 = None
    dict_0 = {}
    object_0 = module_1.object(**dict_0)
    var_0 = module_0.lowestCommonAncestor(none_type_0, none_type_0, object_0)
    tree_node_0 = module_0.TreeNode(float_0, none_type_0, var_0)
    var_1 = module_0.lowestCommonAncestor(tree_node_0, object_0, var_0)
    tree_node_1 = module_0.TreeNode(right=var_1)
    assert tree_node_1.val == 0
    assert tree_node_1.right is None


def test_case_6():
    tree_node_0 = module_0.TreeNode()
    assert tree_node_0.val == 0
    tree_node_1 = module_0.TreeNode()
    assert tree_node_1.val == 0
    var_0 = module_0.lowestCommonAncestor(tree_node_1, tree_node_1, tree_node_1)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "Problem36_GeneratedSolution.TreeNode"
    )
    assert var_0.val == 0
    assert var_0.left is None
    assert var_0.right is None
    object_0 = module_1.object()
    tree_node_2 = module_0.TreeNode(right=object_0)
    assert tree_node_2.val == 0
    var_1 = module_0.lowestCommonAncestor(var_0, tree_node_1, tree_node_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "Problem36_GeneratedSolution.TreeNode"
    )
    assert var_1.val == 0
    assert var_1.left is None
    assert var_1.right is None
    tree_node_3 = module_0.TreeNode(left=tree_node_2, right=var_0)
    assert tree_node_3.val == 0
    tree_node_4 = module_0.TreeNode(var_1, var_1, object_0)
    assert (
        f"{type(tree_node_4.val).__module__}.{type(tree_node_4.val).__qualname__}"
        == "Problem36_GeneratedSolution.TreeNode"
    )
    assert (
        f"{type(tree_node_4.left).__module__}.{type(tree_node_4.left).__qualname__}"
        == "Problem36_GeneratedSolution.TreeNode"
    )
    var_2 = module_0.lowestCommonAncestor(tree_node_3, tree_node_2, var_0)
    assert var_2.val == 0
    assert (
        f"{type(var_2.left).__module__}.{type(var_2.left).__qualname__}"
        == "Problem36_GeneratedSolution.TreeNode"
    )
    assert (
        f"{type(var_2.right).__module__}.{type(var_2.right).__qualname__}"
        == "Problem36_GeneratedSolution.TreeNode"
    )
    tree_node_5 = module_0.TreeNode()
    assert tree_node_5.val == 0
    var_3 = module_1.object()
