def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst = list(phrase)
    for i in range(len(lst)):
        if i == 0 or lst[i - 1] == " ":
            lst[i] =lst[i].upper()
        else:
            lst[i] = lst[i].lower()
    return "".join(lst)
    
