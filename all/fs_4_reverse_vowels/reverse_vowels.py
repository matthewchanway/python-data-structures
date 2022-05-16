def reverse_vowels(s):
    letters = list(s)
    index_list = []
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for a, letter in enumerate(letters):
        if letter in vowels:
            index_list.append(a)
    index_list_copy = index_list.copy()
    index_list_copy.reverse()
    letters_copy = letters.copy()
    for i,indexnum in enumerate(index_list_copy):
        letters[indexnum] = letters_copy[index_list[i]]
    return "".join(letters)


    



    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """