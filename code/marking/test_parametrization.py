import pytest
from rpncalc.utils import calc


# Parametrization preferred over looping inside the test to distinguish between different test cases
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 3),
    (1, 2, 3),
    (2, 3, 5),
])
def test_add(a, b, expected):
    assert calc(a, b, "+") == expected

@pytest.mark.parametrize(
    "op", ["+", "-", "*", "/", "**"])
def test_smoke(op):
    calc(1, 2, op)


# Permuting the test cases, the 4 test cases we will have: test_permutations[3-1], test_permutations[3-2], test_permutations[4-1], test_permutations[4-2]
# This means we cannot use the expected value in the test case
@pytest.mark.parametrize("a", [1, 2])
@pytest.mark.parametrize("b", [3, 4])
def test_permutations(a, b):
    assert calc(a, b, "+") == a + b


# Giving ids to the test cases
@pytest.mark.parametrize(
    "a, b, op, expected", [
    (1, 1, "+", 2),
    (3, 1, "-", 2),
], ids=["1+1", "3-1"]) # Can also pass a callable to generate the id, so that we can have dynamic ids
def test_ids(a, b, expected):
    assert calc(a, b, "+") == expected

# Can also give id at the point of defining the test case
@pytest.mark.parametrize(
    "a, b, op, expected", [
    pytest.param(1, 2, "+", 3, id="1+2"),
    pytest.param(3, 1, "-", 5, id="3-1"), # This is better than the default test id "3-1---5"
])
def test_id_per_test(a, b, op, expected):
    assert calc(a, b, op) == expected

# Using a data class for test parametrization can make the test cases more readable