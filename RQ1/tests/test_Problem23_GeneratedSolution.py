# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Problem23_GeneratedSolution as module_0


def test_case_0():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    var_0 = module_0.reorderDigits(set_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 3233.236
    list_0 = [float_0, float_0]
    var_0 = module_0.reorderDigits(list_0)
    assert var_0 == ""
    var_1 = module_0.reorderDigits(var_0)
    assert var_1 == ""
    var_2 = module_0.reorderDigits(var_0)
    assert var_2 == ""
    var_3 = module_0.reorderDigits(var_1)
    assert var_3 == ""
    none_type_0 = None
    module_0.reorderDigits(none_type_0)
