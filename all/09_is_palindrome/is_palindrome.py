from operator import truediv


def is_palindrome(phrase):
    phrase2 = phrase.replace(" ","")
    rev_list=list(phrase2)
    rev_list.reverse()
    rev_phrase = "".join(rev_list)
    if phrase2.lower() == rev_phrase.lower():
        return True
    else:
        return False
    

    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> print(is_palindrome('Noon'))
        True

        >>> is_palindrome('noon')
        True

        >>> print(is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
