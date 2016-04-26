def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for calculating greatest common divisor of 2 integers.
    see https://en.wikipedia.org/wiki/Euclidean_algorithm for details

    For the best explanation of the algorithm that I have heard/seen watch
    this: https://www.youtube.com/watch?v=wPMZr9RDmVk

    :param a: integer #1
    :param b: integer #2
    :return: GCD
    """
    if a > b:
        x, y = a, b
    else:
        x, y = b, a
    while y != 0:
        t = y
        y = x % y
        x = t
    return x

if __name__ == '__main__':
    try:
        mya = int(input("a: "))
        myb = int(input("b: "))

        print("gcd({0},{1})={2}".format(mya, myb, gcd(mya, myb)))
    except:
        print("Invalid input.")
