# -*- coding: utf-8 -*-
""" Output module EoP_chap10_sub
    
    function :
        puts        -- Output n s continuously
        put_start   -- Output n '*' continuously
"""

def puts(*, n: int, s: str) -> None:
    """ Output n s continuously

    Parameters
    ----------
    n : int
        Number of string that output
    s : str
        String that output

    Returns
    -------
    None
    
    """
    for _ in range(n):
        print(s, end='')
        
def put_star(n: int) -> None:
    """ Output n '*' continuously

    Parameters
    ----------
    n : int
        Number of output

    Returns
    -------
    None

    """
    puts(n=n, s='*')