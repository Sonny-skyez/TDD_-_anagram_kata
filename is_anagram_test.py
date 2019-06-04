from is_anagram import is_anagram


def test_initial():
    assert is_anagram('test', 'test')


def test_not_anagram():
    assert not is_anagram('test', 'not test')