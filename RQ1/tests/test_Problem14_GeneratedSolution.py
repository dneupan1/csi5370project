# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Problem14_GeneratedSolution as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0}
    str_0 = "cR]f67yJX = 1P0"
    var_0 = module_0.getMaxRepetitions(str_0, set_0, set_0, bool_0)
    assert var_0 == 0
    module_0.getMaxRepetitions(str_0, var_0, str_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "\ts~Yq0aNrE"
    module_0.getMaxRepetitions(str_0, str_0, str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b"\x82\xcc\x9f&\x91{\x01I\x18\x93\x98D\x14\xab`"
    var_0 = module_0.getMaxRepetitions(bytes_0, bool_0, bytes_0, bool_0)
    assert var_0 == 1
    none_type_0 = None
    module_0.getMaxRepetitions(none_type_0, var_0, var_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    str_0 = "cR]f67yJX = 1P0"
    module_0.getMaxRepetitions(str_0, bool_0, str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -318.0
    str_0 = "WAh&f6,}jQ"
    bool_0 = False
    tuple_0 = (float_0, str_0, str_0, bool_0)
    list_0 = [bool_0, float_0, str_0, float_0]
    module_0.getMaxRepetitions(tuple_0, bool_0, list_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "WAh&f6,}jQ"
    bool_0 = False
    tuple_0 = (bool_0, str_0, str_0, bool_0)
    list_0 = [bool_0, bool_0, str_0, bool_0]
    module_0.getMaxRepetitions(tuple_0, bool_0, list_0, tuple_0)
