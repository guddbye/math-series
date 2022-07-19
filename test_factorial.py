from factorial_module import factorial

def test_factorial_input_1():
    actual = factorial(1)
    expected = 1
    assert actual == expected