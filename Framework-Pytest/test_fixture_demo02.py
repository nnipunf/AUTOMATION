import pytest

@pytest.yield_fixture()
def setup():
    print('Browser Launch Successfully.')

    yield
    print('Browser closed')


def test_login_tc001(setup):
    print('valid Login done.')


def test_login_tc002(setup):
    print('invalid login done.')
