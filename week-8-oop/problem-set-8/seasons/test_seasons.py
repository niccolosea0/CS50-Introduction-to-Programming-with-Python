from seasons import get_date
import pytest

def test_invalid_date():
    with pytest.raises(SystemExit):
        get_date("Text")

def test_invalid_format():
    with pytest.raises(SystemExit):
        get_date("1990 05 13")
