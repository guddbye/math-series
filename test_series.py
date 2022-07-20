from series import fibonacci, lucas


def test_fibonacci_input0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_input2():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_fibonacci_input3():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected
