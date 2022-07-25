# factorial = the product of positive integers up to and including given integer
# factorial(1) = 1
# factorial(2) = 2
# factorial(3) = 6
# above notes from class

def fibonacci(n):
    """
    Returns the nth fibonacci number in the series.\n
    Requires an integer input representing the index in the series.\n
    Index starts at 0: [0, 1, 1, 2, 3, 5, ...]
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) \
           + fibonacci(n - 2)

    if __name__ == '__main__':
        num: int = int(input('>'))
        print(fibonacci(n))


def lucas(n):
    """
    Returns the nth lucas number in the series.\n
    Requires an integer input representing the index in the series.\n
    Index starts at 0: [2, 1, 3, 4, 7, ...]
    """
    if n == 0:
        return 2
    if n == 1:
        return 1

    return lucas(n - 1) \
           + lucas(n - 2)

    if __name__ == '__main__':
        num = int(input('>'))
        print(lucas(n))


def sum_series(n, a=0, b=1):
    """
    Returns the nth number in the series created by summing the previous two numbers in the series.\n
    Requires an integer input representing the index in the series.\n
    Optionally accepts two additional parameters representing first two numbers in the series.
    Default values for optional parameters correspond to the first two numbers in the fibonacci sequence.\n
    Index starts at 0: first=0, second=1, ..., [n-1] + [n-2]
    """
    if n == 0:
        return a
    if n == 1:
        return b

    return sum_series(n - 1, a, b) \
           + sum_series(n - 2, a, b)
