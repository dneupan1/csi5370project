# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Problem24_GeneratedSolution as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 1519.535379
    module_0.findTargetSumWays(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 2904
    set_0 = {int_0}
    var_0 = module_0.findTargetSumWays(set_0, int_0)
    assert var_0 == 1
    module_1.object(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1252
    set_0 = set()
    var_0 = module_0.findTargetSumWays(set_0, int_0)
    assert var_0 == 0
    module_0.findTargetSumWays(int_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2904
    set_0 = {int_0}
    var_0 = module_0.findTargetSumWays(set_0, int_0)
    assert var_0 == 1
    var_1 = module_0.findTargetSumWays(set_0, var_0)
    assert var_1 == 0
    str_0 = "Q(l'$\x0bZ[nsE5"
    module_0.findTargetSumWays(var_0, str_0)
