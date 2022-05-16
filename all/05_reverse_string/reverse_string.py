def reverse_string(phrase):
    phrase_lst = list(phrase)
    phrase_lst_rev = phrase_lst[::-1]
    return "".join(phrase_lst_rev)

    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
