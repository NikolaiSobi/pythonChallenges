#!/usr/bin/env python3
def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dict = {}
    for ltr in phrase:
        dict.update({ltr: phrase.count(ltr)})

    return dict

print(multiple_letter_count('Yay'))