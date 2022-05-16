def same_frequency(num1, num2):
    num1str = str(num1)
    num2str = str(num2)
    for char in num1str:
        if num1str.count(char) != num2str.count(char):
            return False
    return True

    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """