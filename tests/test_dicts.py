from utils import dicts


def test_get_val():
    assert dicts.get_val({'Name': 'Denis', 'Surname': 'Volchkov'}, 'Name') == 'Denis'
    assert dicts.get_val({}, 'Name') == 'git'
    assert dicts.get_val({'Name': 'Denis', 'Surname': 'Volchkov'}, 'FirstName') == 'git'
