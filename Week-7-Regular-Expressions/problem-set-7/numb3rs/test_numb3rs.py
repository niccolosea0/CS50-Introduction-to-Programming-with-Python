import pytest
from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_str():
    assert validate("cat") == False

def test_high_numbers():
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False

def test_leading_zeros():
    assert validate("192.168.001.1") == False
    assert validate("001.002.003.004") == False

def test_long_length():
    assert validate("192.168.001.1.156") == False

def test_short_length():
    assert validate("192.186") == False
    assert validate("0.45.77") == False
