def vowel_count(phrase):
    dict = {}
    phrase_lower = phrase.lower()
    vowels = "aeiou"
    for char in phrase_lower:
        if char in vowels:
            if char in dict:
                dict[char] = dict[char] + 1
            else:
                dict[char] = 1
    return dict



    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """