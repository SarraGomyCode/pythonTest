import pytest


def function(x):
    return x+1
def text_print():
    print("first test")
def test_example ():
    assert function(3) == 4

@pytest.mark.parametrize("a,b,final", [(2,3,2), (4,8,6),(2,2,4)])
def param_test (a,b,final):
    assert a + b == final