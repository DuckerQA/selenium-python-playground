import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo1(self):
        print("Hello World1")

    def test_fixtureDemo2(self):
        print("Hello World2")

    def test_fixtureDemo3(self):
        print("Hello World3")

    def test_fixtureDemo4(self):
        print("Hello World4")