import pytest
from rpncalc.utils import calc

def test_add():
    res = calc(1, 3, "+")
    assert res == 4

@pytest.mark.xfail(reason="Power operation is not implemented yet. See #1234")
def test_power():
    res = calc(2, 3, "**")
    assert res == 8
# Tests which are marked as expected to fail but pass will be reported as XPASS(X) in the test summary
# However, by default, they will be reported as PASSED.
# To report them as FAILED, use xfail_strict=True in the pytest.ini file