import pytest
from twttr import shorten

def test_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"

def test_lowercase_vowels():
    assert shorten("amadeo") == "md"

def test_punctuation():
    assert shorten("hello, world") == "hll, wrld"

def test_numbers():
    assert shorten("Hello123") == "Hll123"
