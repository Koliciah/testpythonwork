from bank import value

def test():
    assert value("Hello") == 0
    assert value(" hello") == 0
    assert value("HELLO ") == 0
    assert value("Hey") == 20
    assert value("hi") == 20
    assert value("Greetings") == 100
