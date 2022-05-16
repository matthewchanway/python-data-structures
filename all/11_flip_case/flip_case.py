def flip_case(phrase, to_swap):
    phrase_list = list(phrase)
    swap_list = []
    for letter in phrase_list:
        if letter.lower() == to_swap.lower() and letter.isupper():
            swap_list.append(letter.lower())
        if letter.lower() == to_swap.lower() and letter.islower():
            swap_list.append(letter.upper())
        if letter.lower() != to_swap.lower() :
            swap_list.append(letter)
    
    return "".join(swap_list)

print(flip_case('Aaaahhh', 'a'))


    # """Flip [to_swap] case each time it appears in phrase.

    #     >>> print(flip_case('Aaaahhh', 'a'))
    #     'aAAAhhh'

    #     >>> print(flip_case('Aaaahhh', 'A'))
    #     'aAAAhhh'

    #     >>> print(flip_case('Aaaahhh', 'h'))
    #     'AaaaHHH'

    # """
    # swap_list = [letter.lower() if letter == 'l' and letter.isupper() for letter in phrase_list]
