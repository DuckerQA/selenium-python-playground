#Any pytest file should start with test_ or end with _test
#pytest method names should start with test_
import pytest

@pytest.mark.smoke
# @pytest.mark.skip
def test_pytest_program():
    msg = "Hello"
    assert msg == "Hi", "Test failed"

# @pytest.mark.skip
def test_second_programCreditCard():
    a = 4
    b = 5
    assert a+ 1 == b, "Test Passed"


@pytest.mark.runMe
def test_fixture_test_here(setup):
    print("Hohohohoo")