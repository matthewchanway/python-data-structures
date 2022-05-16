def three_odd_numbers(nums):

    for index, num in enumerate(nums):
        if index > 1:
            if (num + nums[index-1] + nums[index-2]) % 2 != 0:
                return True
    return False

    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
