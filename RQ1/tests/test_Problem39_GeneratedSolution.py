# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Problem39_GeneratedSolution as module_0


def test_case_0():
    str_0 = "c_]Vz"
    var_0 = module_0.removeInvalidParentheses(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.removeInvalidParentheses(none_type_0)


def test_case_2():
    str_0 = "75()"
    var_0 = module_0.removeInvalidParentheses(str_0)


def test_case_3():
    str_0 = "5()(YF"
    var_0 = module_0.removeInvalidParentheses(str_0)


def test_case_4():
    str_0 = "+.z)"
    var_0 = module_0.removeInvalidParentheses(str_0)


def test_case_5():
    str_0 = "5(s)\\\r`)^\r6l"
    var_0 = module_0.removeInvalidParentheses(str_0)
    list_0 = [str_0]
    var_1 = module_0.removeInvalidParentheses(var_0)
    var_2 = module_0.removeInvalidParentheses(list_0)
