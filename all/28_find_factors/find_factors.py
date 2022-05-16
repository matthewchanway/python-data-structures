def find_factors(num):
    res = []
    factors = range(num)
    for factor in factors[1:]:
        if num % factor == 0:
            res.append(factor)
    res.append(num)
    return res

    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
