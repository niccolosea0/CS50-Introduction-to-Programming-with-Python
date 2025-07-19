import pytest
from working import convert


def test_without_colon():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"

def test_with_colons():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"

def test_with_one_colon():
    assert convert("10:00 PM to 7 AM") == "22:00 to 07:00"
    assert convert("7:00 AM to 10 PM") == "07:00 to 22:00"

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

