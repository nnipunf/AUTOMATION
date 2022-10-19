import pytest

@pytest.yield_fixture()
def setup():
    print('Browser Launch Successfully.')

    yield
    print('Browser closed')

@pytest.mark.order(2)
def test_login_tc001(setup):
    print('valid Login done.')

@pytest.mark.order(1)
def test_login_tc002(setup):
    print('invalid login done.')
