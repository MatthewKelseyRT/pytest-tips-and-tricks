import pytest
from rpncalc.utils import calc


@pytest.mark.parametrize(
    "a, b, op, expected", [
    pytest.param(
        2, 3, "**", 8,
        marks=pytest.mark.xfail(reason="..."), # This test case is expected to fail, xfail means expected to fail
    ),
    (1, 2, "+", 3),
    (3, 1, "-", 5),
])
def test_calc(a, b, op, expected):
    assert calc(a, b, op) == expected