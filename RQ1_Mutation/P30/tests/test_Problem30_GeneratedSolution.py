# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Problem30_GeneratedSolution as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "mHK_&I5G0o>3"
    module_0.exist(str_0, str_0)


def test_case_1():
    set_0 = set()
    var_0 = module_0.exist(set_0, set_0)


def test_case_2():
    str_0 = "WM'"
    list_0 = [str_0, str_0, str_0]
    list_1 = [str_0, list_0]
    var_0 = module_0.exist(list_1, list_1)
    assert var_0 is False


def test_case_3():
    str_0 = "WM'"
    list_0 = [str_0, str_0, str_0]
    list_1 = [str_0, list_0]
    var_0 = module_0.exist(list_1, list_0)
    assert var_0 is True


def test_case_4():
    str_0 = "hQ'"
    list_0 = [str_0, str_0, str_0, str_0]
    list_1 = [list_0]
    var_0 = module_0.exist(list_1, list_0)
    assert var_0 is True


def test_case_5():
    str_0 = "/4WM'"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    list_1 = [str_0, list_0, list_0]
    var_0 = module_0.exist(list_1, list_0)
    assert var_0 is True
