from working import convert
import pytest

def test_time():
    assert convert ("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert ("8:30 AM to 4:30 PM") == "08:30 to 16:30"
    assert convert ("7:15 AM to 2:45 PM") == "07:15 to 14:45"

def test_meridiem_time():
    assert convert ("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert ("12 PM to 12 AM") == "12:00 to 00:00"

def test_invalid():
    with pytest.raises(ValueError):
        convert("2:75 AM to 3:80 PM")
    with pytest.raises(ValueError):
        convert("1 AM - 3 AM")
    with pytest.raises(ValueError):
        convert("18:75 AM to 13:00 AM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")


