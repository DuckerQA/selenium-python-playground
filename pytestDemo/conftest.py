import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be exectued first")
    yield
    print("wil be run after test")

@pytest.fixture()
def data_load():
    print("user profile data is being created")
    return ["Mateo", 'Crocodillo', 'mateo@crocodillo.com']

@pytest.fixture(params=["chrome", "firefox", "IE"])
def crossBrowser(request):
    return request.param