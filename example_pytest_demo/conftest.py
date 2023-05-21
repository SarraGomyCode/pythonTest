import pytest


#@pytest.fixture(scope="session",autouse=True)
def setUp():
    print("open browser")
    print("login")
    print("connect")
    yield
    print("logout")
    print("disconnect")