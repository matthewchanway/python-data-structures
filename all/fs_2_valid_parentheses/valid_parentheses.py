def valid_parentheses(parens):
    open = []
    close = []
    quote = []
    for char in parens:
        if char == "(":
            open.append(char)
        if char == ")":
            close.append(char)
    if len(open) == len(close) and parens[-1] == ")":
        return True
    else:
        return False
    




    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """