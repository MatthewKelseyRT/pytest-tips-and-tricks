import pytest
from rpncalc.utils import calc


def test_add():
    res = calc(0.2, 0.1, "+")
    assert res == pytest.approx(0.3)

# Can override tolerance (rel/abs), e.g. 20 ± 2°:
# assert temperature == pytest.approx(20, abs=2)