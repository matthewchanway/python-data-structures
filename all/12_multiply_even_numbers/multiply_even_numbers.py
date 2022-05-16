def multiply_even_numbers(nums):
    evens = [n for n in nums if n % 2 == 0]
    sum = 0
    for num in evens:
        if num % 2 == 0 and sum == 0:
            sum = num
        elif num % 2 == 0 and sum > 0:
            sum = sum * num
    if sum == 0:
        return 1
    else:
        return sum
        

print(multiply_even_numbers([2, 3, 4, 5, 6]))
print(multiply_even_numbers([3, 4, 5]))
print(multiply_even_numbers(([1, 3, 5])))




    # """Multiply the even numbers.
    
    #     >>> print(multiply_even_numbers([2, 3, 4, 5, 6]))
    #     48
        
    #     >>> print(multiply_even_numbers([3, 4, 5]))
    #     4
        
    # If there are no even numbers, return 1.
    
    #     >>> print(multiply_even_numbers(([1, 3, 5]))
    #     1
    # """