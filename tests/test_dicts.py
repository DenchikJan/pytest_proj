import pytest

from utils import dicts


@pytest.fixture
def arrs_fixture():
    return {'Name': 'Denis', 'Surname': 'Volchkov'}


def test_get_val(arrs_fixture):
    assert dicts.get_val(arrs_fixture, 'Name') == 'Denis'
    assert dicts.get_val({}, 'Name') == 'git'
    assert dicts.get_val(arrs_fixture, 'FirstName') == 'git'
