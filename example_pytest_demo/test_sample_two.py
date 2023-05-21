import pytest


def test_fixture_function():
    print("connected with success")

def test_fixture_second_function():
        print("you don't have access")
def function(x):
    return x+1
def test_example ():
    assert function(3) == 4