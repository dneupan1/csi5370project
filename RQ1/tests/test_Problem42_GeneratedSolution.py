# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Problem42_GeneratedSolution as module_0


def test_case_0():
    bytes_0 = b'm\xc9"}\xe5\x86\xef\xb9T20i\x87\xd2O\xa3j'
    bool_0 = False
    var_0 = module_0.mergeStones(bytes_0, bool_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.mergeStones(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    bool_1 = False
    var_0 = module_0.mergeStones(list_0, bool_1)
    assert var_0 == -1
    var_1 = module_0.mergeStones(list_0, var_0)
    assert var_1 == -1
    module_0.mergeStones(bool_1, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -2286.38
    bytes_0 = b'm\xc9\x9c"\xcf}\xe5\x86t\xb9T20i\x87\xd2O\xa3j'
    var_0 = module_0.mergeStones(bytes_0, float_0)
    assert var_0 == -1
    bool_0 = False
    var_1 = module_0.mergeStones(bytes_0, bool_0)
    assert var_1 == -1
    module_0.mergeStones(float_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -2286.38
    bytes_0 = b'm\xc9\x9c"\xcf}\xe5\x86t\xb9T20i\x87\xd2O\xa3j'
    var_0 = module_0.mergeStones(bytes_0, float_0)
    assert var_0 == -1
    int_0 = 3
    var_1 = module_0.mergeStones(bytes_0, int_0)
    assert var_1 == 6705
    module_0.mergeStones(int_0, var_1)
