from plates import is_valid

def test_len():
    assert is_valid("AB") is True
    assert is_valid("AB25") is True
    assert is_valid("ABAB25") is True
    assert is_valid("A") is False
    assert is_valid("ABABABAB") is False

def test_num():
    assert is_valid("AB25") is True
    assert is_valid("ABAB25") is True
    assert is_valid("A123") is False
    assert is_valid("12AB") is False
    assert is_valid("AB25AB") is False


def test_zero():
    assert is_valid("AB10") is True
    assert is_valid("AB01") is False

def test_punc():
    assert is_valid("AB25") is True
    assert is_valid("AA.20") is False
    assert is_valid("AB AA") is False

def test_let():
    assert is_valid("AB25") is True
    assert is_valid("A125") is False
    assert is_valid("25AB") is False


