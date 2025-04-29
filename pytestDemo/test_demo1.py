#Any pytest file should start with test_ or end with _test
#pytest method names should start with test_
import pytest

@pytest.mark.runMe
def test_first_pytest_program(setup):
    print("Hello World")

@pytest.mark.xfail
def test_first_pytest_programCreditCard():
    print("Hello World")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
