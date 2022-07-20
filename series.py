# factorial = the product of positive integers up to and including given integer
# factorial(1) = 1
# factorial(2) = 2
# factorial(3) = 6
# above notes from class

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) \
           + fibonacci(n - 2)

    if __name__ == '__main__':
        num: int = int(input('>'))
        print(fibonacci(n))


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1

    return lucas(n - 1) \
           + lucas(n - 2)

    if __name__ == '__main__':
        num = int(input('>'))
        print(lucas(n))
