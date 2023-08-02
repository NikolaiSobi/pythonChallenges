#!/usr/bin/env python3
def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    copy_list = [i for i in lst if i]
    return copy_list

