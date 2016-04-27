import math


def is_prime(n):
    """returns True if n is prime"""
    if n % 1 > 0 or n < 2:
        return False
    if n == least_factor(n):
        return True
    return False


def largest_prime_factor(n):
    """
    returns the largest prime factor of n
    The prime factors of 13195 are 5, 7, 13 and 29
    the largest is 29

    :param n: number
    :return: largest prime factor
    """
    lpf, x = 2, n
    while x > lpf:
        if x % lpf == 0:
            x //= lpf
            lpf = 2
        else:
            lpf += 1
    return lpf


def least_factor(n):
    """
    Find the least factor of n
    :param n: integer value
    :return: least factor as integer
    """
    if n == 0:
        return 0
    if n % 1 > 0 or n * n < 2:
        return 1
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5
    m = math.sqrt(n)
    i = 7
    while i <= m:
        if n % i == 0:
            return i
        if n % (i + 4) == 0:
            return i + 4
        if n % (i + 6) == 0:
            return i + 6
        if n % (i + 10) == 0:
            return i + 10
        if n % (i + 12) == 0:
            return i + 12
        if n % (i + 16) == 0:
            return i + 16
        if n % (i + 22) == 0:
            return i + 22
        if n % (i + 24) == 0:
            return i + 24
        i += 30
    return n

# def is_pandigital(n):

