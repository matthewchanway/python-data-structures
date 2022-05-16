def mode(nums):
    list = []
    for num in nums:
        list.append([num, nums.count(num)])
    list.sort(reverse=True,key=lambda x: x[1])
    return list[0][0]




    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> print(mode([1, 2, 1]))
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
