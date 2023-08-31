import pytest

from utils import arrs


@pytest.fixture
def arrs_fixture():
    return [1, 2, 3, 4]


def test_get(arrs_fixture):
    assert arrs.get(arrs_fixture, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(arrs_fixture):
    assert arrs.my_slice(arrs_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(arrs_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(arrs_fixture, end=2) == [1, 2]
