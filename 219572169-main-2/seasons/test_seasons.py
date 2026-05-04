from datetime import date
from seasons import birthdate
import pytest

def test():
    assert "minutes" in birthdate(date(2013, 10, 10))
    assert "minutes" in birthdate(date(1999, 9, 9))
    assert "minutes" in birthdate(date(2020, 1, 1))

def test_fail():
    with pytest.raises(TypeError):
        birthdate("Janaury 1, 2009")



