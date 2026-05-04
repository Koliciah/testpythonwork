from numb3rs import validate
import pytest

def test_true():
    assert validate ("100.2.3.4") is True
    assert validate ("255.255.255.255") is True

def test_false():
    assert validate ("266.1.2.3") is False
    assert validate ("1.2.3.4.5.6") is False
    assert validate ("-1.3.4.5") is False
    assert validate ("1.2") is False
    assert validate ("252.266.22.4") is False
