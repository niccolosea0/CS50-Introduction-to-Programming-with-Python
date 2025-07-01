import pytest
from plates import is_valid

def test_has_first_two_characters():
    assert is_valid("ab") == True
    assert is_valid("123") == False
    assert is_valid("1") == False


def test_has_proper_size():
    assert is_valid("abcdef") == True
    assert is_valid("abcdefg") == False
    assert is_valid("a") == False

def test_ends_with_numbers():
    assert is_valid("ab123") == True
    assert is_valid("ab12cd") == False

def test_zero_is_not_first_number():
    assert is_valid("ab102") == True
    assert is_valid("ab012") == False

def test_isalnum():
    assert is_valid("cs50") == True
    assert is_valid("cs!@#") == False
    assert is_valid("cs@@50") == False
