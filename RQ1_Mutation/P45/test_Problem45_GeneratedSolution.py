# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import collections as module_0
import Problem45_GeneratedSolution as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    defaultdict_0 = module_0.defaultdict()
    tuple_0 = (defaultdict_0,)
    module_1.findItinerary(tuple_0)


def test_case_1():
    defaultdict_0 = module_0.defaultdict()
    var_0 = module_1.findItinerary(defaultdict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 711.2
    module_1.findItinerary(float_0)
