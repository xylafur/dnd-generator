import random


class InvalidRangeException(Exception): pass
class InvalidArgumentsException(Exception): pass


def roll_die(count, die, advantage=False, disadvantage=False, total=True):
    """
        Generates a random number between 1 and die value.

        Args:
             count (:class: `int`):  The upper bound of the random range.
             die (:class: `int`):  How many random numbers to generate.

        Kargs:
            advantage (:class: `bool`):  If True, generates two numbers and
                takes the largest of the two.

            disadvantage (:class: `bool`):  If True, generates two numbers and
                takes the smallest of the two.

            total (:class: `bool`):  If True, returns a single int as a total of
                all generated numbers.  If False, generates numbers
                individually.  Defaults to True.

        Raises:
            (:class: `InvalidRangeException`):  If the range is less than 4.
                If the count is less than or equal to 0.

            (:class: `InvalidArgumentException`):  If the die is not a d20, and
                advantage or disadvantage is True.

                If a die is a d20 and total is True.

        Returns:
            (:class: `int` or `list`):  Returns an int if total is True, returns
                a list if total is False.
    """
    # Sanity check the arguments.
    if count <= 0:
        raise InvalidRangeException("Must provide a count greater than 0.")

    if die <= 3:
        raise InvalidRangeException("Must provide a range greater than 3.")

    # Having advantage and disadvantage cancel each other out.
    if advantage and disadvantage:
        advantage = False
        disadvantage = False

    if (advantage or disadvantage) and die != 20:
        raise InvalidArgumentsException("You cannot have advantage/disadvantage"
                                        " on a non-d20 roll.")

    if die == 20 and total is True:
        raise InvalidArgumentsException("You cannot total d20 rolls.")

    total_result = 0
    individual_result = []

    for i in range(1, count):
        num = random.randint(1, die)

        if advantage is True:
            num2 = random.randint(1, die)
            individual_result.append(max(num, num2))

        elif disadvantage is True:
            num2 = random.randint(1, die)
            individual_result.append(min(num, num2))

        total_result += num

    if total:
        return total_result
    else:
        return individual_result


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
    return roll_die(count, 4, total=total)


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
    return roll_die(count, 6, total=total)


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
    return roll_die(count, 8, total=True)


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
    return roll_die(count, 10, total=True)


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


def roll_d20(count, advantage=False, disadvantage=False):
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

        Returns:
            (:class: `int` or `list`):  Returns an int if total is True, returns
                a list if total is False.
    """
    return roll_die(count, 20,
                    advantage=advantage,
                    disadvantage=disadvantage,
                    total=False)


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
    return roll_die(count, 100, total=total)
