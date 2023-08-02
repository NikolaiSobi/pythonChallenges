#!/usr/bin/env python3
def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_list = list(phrase)
    for i in range(len(phrase_list)):
        if phrase_list[i] == to_swap.upper():
            phrase_list[i] = to_swap.lower()
        elif phrase_list[i] == to_swap.lower():
            phrase_list[i] = to_swap.upper()

    return "".join(phrase_list)



