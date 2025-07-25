from jar import Jar


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5, f"Expected size 5, got {jar.size}"


def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2, f"Expected size 2, got {jar.size}"


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == '🍪' * 0
