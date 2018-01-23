

from random import randint as r

def roll_event(die_num, event_list):
    # TO-DO, why wasnt this implemented yet? It is called in life_story.py
    raise NotImplementedError('This function not yet implemented')


# roll functions
roll_d      = lambda n:r(1,n)   # roll a dice : [1,n]
roll_d0     = lambda n:r(0,n-1) # roll a dice : [0,n-1]
roll_d_adv  = lambda n:max(roll_d(n), roll_d(n))   # roll a dice with adv
roll_d0_adv = lambda n:max(roll_d0(n), roll_d0(n)) # roll a 0dice with adv
roll_d_dis  = lambda n:min(roll_d(n), roll_d(n)) # roll a dice with dis
roll_d0_dis = lambda n:min(roll_d(n), roll_d(n)) # roll a 0dice with dis

def roll_die(die, count=1, adv=False, dis=False, total=True):
    """
        Generates a random number between 1 and die value

        Args:
            die (:class: `int`) Upper bound of die rolls
        Kargs:
            count (:class: `int`) Number of dice rolls, default=1, if count==1
                returns a int instead of list

            adv (:class: `bool`):  If true, takes max of 2 rolls

            dis (:class: `bool`):  If True, generates two numbers and
                takes the smallest of the two.

            total (:class: `bool`):  If True, returns int sum of generated
                numbers. If False, returns list of length @count, of rolls

        Returns:
            int or list, see total parameter, if 
    """
    assert(die > 0)
    assert(count >= 1)

    if adv != dis:
        if adv: # advantage
            ret = [roll_d_adv(die) for i in range(count)]
        else:   # dis
            ret = [roll_d_dis(die) for i in range(count)]

    else: # advantage and disadvantage cancel out in 5e
        ret = [ roll_d(die) for i in range(count) ]

    return sum(ret) if (total or count==1) else ret

def roll_d4(count, total=True):
    """
        Generates a random number between 1 and 4.

        Wrapper function.

        Args:
            count (:class: `int`):  How many random numbers to generate.

        Kargs:
            total (:class: `bool`):  If True, returns a single int as a total of
                all generated numbers.  If False, generates numbers
                individually.  Defaults to True.

        Returns:
            (:class: `int` or `list`):  Returns an int if total is True, returns
                a list if total is False.
    """
    return roll_die(4, count=count, total=total)


def roll_d6(count, total=True):
    """
        Generates a random number between 1 and 6.

        Wrapper function.

        Args:
            count (:class: `int`):  How many random numbers to generate.

        Kargs:
            total (:class: `bool`):  If True, returns a single int as a total of
                all generated numbers.  If False, generates numbers
                individually.  Defaults to True.

        Returns:
            (:class: `int` or `list`):  Returns an int if total is True, returns
                a list if total is False.
    """
    return roll_die(6, count=count, total=total)


def roll_d8(count, total=True):
    """
        Generates a random number between 1 and 8.

        Wrapper function.

        Args:
            count (:class: `int`):  How many random numbers to generate.

        Kargs:
            total (:class: `bool`):  If True, returns a single int as a total of
                all generated numbers.  If False, generates numbers
                individually.  Defaults to True.

        Returns:
            (:class: `int` or `list`):  Returns an int if total is True, returns
                a list if total is False.
    """
    return roll_die(8, count=count, total=True)


def roll_d10(count, total=True):
    """
        Generates a random number between 1 and 10.

        Wrapper function.

        Args:
            count (:class: `int`):  How many random numbers to generate.

        Kargs:
            total (:class: `bool`):  If True, returns a single int as a total of
                all generated numbers.  If False, generates numbers
                individually.  Defaults to True.

        Returns:
            (:class: `int` or `list`):  Returns an int if total is True, returns
                a list if total is False.
    """
    return roll_die(10, count=count, total=True)


def roll_d12(count, total=True):
    """
        Generates a random number between 1 and 12.

        Wrapper function.

        Args:
            count (:class: `int`):  How many random numbers to generate.

        Kargs:
            total (:class: `bool`):  If True, returns a single int as a total of
                all generated numbers.  If False, generates numbers
                individually.  Defaults to True.

        Returns:
            (:class: `int` or `list`):  Returns an int if total is True, returns
                a list if total is False.
    """
    return roll_die(count, 12, total=total)


def roll_d20(count, advantage=False, disadvantage=False, total=False):
    """
        Generates a random number between 1 and 20.

        Wrapper function.

        Args:
            count (:class: `int`):  How many random numbers to generate.

        Kargs:
            advantage (:class: `bool`):  If True, generates two numbers and
                takes the largest of the two.

            disadvantage (:class: `bool`):  If True, generates two numbers and
                takes the smallest of the two.

            total (:class: `bool`):  If True, returns a single int as a total of
                all generated numbers.  If False, generates numbers
                individually.  Defaults to True.

        Returns:
            (:class: `int` or `list`):  Returns an int if total is True, returns
                a list if total is False.
    """
    return roll_die(20, count, adv, dis, total)

def roll_d100(count, total=True):
    """
        Generates a random number between 1 and 100.
        Can also be used as a percentage die.

        Wrapper function.

        Args:
            count (:class: `int`):  How many random numbers to generate.

        Returns:
            (:class: `int` or `list`):  Returns an int if total is True, returns
                a list if total is False.
    """
    return roll_die(100, count=count, total=total)
