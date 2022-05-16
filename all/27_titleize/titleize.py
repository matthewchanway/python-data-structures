def titleize(phrase):
    phrase_lower = phrase.lower()
    a = phrase_lower.split()
    res = []
    for item in a:
        res.append(item.capitalize())
    return " ".join(res)





    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
