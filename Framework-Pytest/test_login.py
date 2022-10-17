import pytest

def test_login_valid():
    print('Login successful, Test passed')

def test_login_invalid():
    print('Login failed, Test passed')

def test_forcefullyFailed():
    assert False