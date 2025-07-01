import pytest
from bank import value

def test_hello_lowercase():
    assert value("hello") == 0

def test_hello_uppercase():
    assert value("Hello") == 0

def test_h_lowercase():
    """ if greeting starts with 'h' return value should be 20 """
    assert value("hi") == 20
    assert value("hey") == 20

def test_h_uppercase():
     """ if greeting starts with 'H' return value should be 20 """
     assert value("Hi") == 20
     assert value("Hey") == 20

def test_without_h():
    """ If does not start's with 'h'/'H' return 100 """
    assert value("Friend") == 100
    assert value("Sister") == 100

def test_without_h_start():
    """ If h is in text but not in the start """
    assert value("What's up?") == 100
    assert value("Welcome to home") == 100

def test_number():
    assert value("1010") == 100
