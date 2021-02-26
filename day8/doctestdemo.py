def equals(a,b):


    """
    >>> equals(2,2)=="Equal"
    True
    >>> equals(2,3)=="Not Equal"
    True
    >>> equals(2,3)=="Equal"
    False

    """
    if a==b:
        return "Equal"
    else:
        return "Not Equal"

import doctest
doctest.testmod()
#py doctestdemo.py