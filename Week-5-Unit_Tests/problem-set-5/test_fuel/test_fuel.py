import pytest
from fuel import convert
from fuel import gauge

def test_valid_return():
    assert convert("3/4") == 75
    assert convert("2/4") == 50

def test_integers():
    with pytest.raises(ValueError):
        convert("2.2/3")

    with pytest.raises(ValueError):
        convert("3/4.5")

def test_positive_integers():
    with pytest.raises(ValueError):
        convert("-1/4")

    with pytest.raises(ValueError):
        convert("3/-4")

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_first_is_greater():
    with pytest.raises(ValueError):
        convert("5/2")

def test_label_for_below_one():
    assert gauge(1) == "E"
    assert gauge(0.75) == "E"

def test_label_for_greater_99():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_label_for_number():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
