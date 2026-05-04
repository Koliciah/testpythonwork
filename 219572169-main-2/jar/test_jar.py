from jar import Jar
import pytest


def test_init():
     jar = Jar()
     assert jar.capacity == 12
     assert jar.cookies == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.cookies == 2
    jar.deposit(2)
    assert jar.cookies == 4
    with pytest.raises(ValueError):
        jar.deposit(5)



def test_withdraw():
    jar = Jar(7)
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.cookies == 3
    jar.withdraw(1)
    assert jar.cookies == 2
    with pytest.raises(ValueError):
        jar.withdraw(7)
