from um import count
import pytest

def test_um():
    assert count ("um") == 1
    assert count ("UM") == 1
    assert count ("UM, hi are you um doing today") == 2


def test_not():
    assert count ("yum") == 0
    assert count ("album") == 0
    assert count ("ummm") == 0

