# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Problem33_GeneratedSolution as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    complex_0 = 4345 - 1361.38671j
    module_0.rob_linear(complex_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    var_0 = module_0.rob_linear(none_type_0)
    assert var_0 == 0
    var_1 = module_0.rob_linear(none_type_0)
    assert var_1 == 0
    var_2 = module_0.rob_linear(none_type_0)
    assert var_2 == 0
    set_0 = {var_2, var_2, var_0}
    module_0.rob(set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = 249.985907 + 43.711j
    dict_0 = {complex_0: complex_0}
    var_0 = module_0.rob_linear(dict_0)
    assert var_0 == (249.985907 + 43.711j)
    str_0 = "Y#z'1'Uqd@\t#iWSI'="
    var_1 = module_0.rob(str_0)
    assert var_1 == "zY"
    module_0.rob(dict_0)


def test_case_3():
    float_0 = -1485.483602
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.rob(list_0)
    assert var_0 == pytest.approx(-1485.483602, abs=0.01, rel=0.01)


def test_case_4():
    float_0 = -735.476
    set_0 = {float_0, float_0, float_0}
    var_0 = module_0.rob_linear(set_0)
    assert var_0 == pytest.approx(-735.476, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "u2MF4\x0b\tUB;-c~{"
    var_0 = module_0.rob(str_0)
    assert var_0 == "~u"
    none_type_0 = None
    var_1 = module_0.rob(var_0)
    assert var_1 == "~"
    module_0.rob(none_type_0)
