from rpncalc.utils import calc

import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        calc(3, 0, "/")

def test_invalid_operator():
    with pytest.raises(ValueError):
        calc(3, 0, "%")

def test_invalid_operator_regex_match():
    with pytest.raises(ValueError, match=r"Invalid operator"):
        calc(3, 0, "%")

def test_invalid_operator_as():
    with pytest.raises(ValueError) as excinfo:
        calc(3, 0, "%")
    assert str(excinfo.value) == "Invalid operator: %"