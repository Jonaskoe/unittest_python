"""Main Module.
"""
from typing import Union


def add(first: Union[int, float], second: Union[int, float]) -> Union[int, float]:
    """Add two numbers.

    Arguments:
        first {Union[int, float]} -- First number.
        second {Union[int, float]} -- second number.

    Raises:
        TypeError: first has to be a number.
        TypeError: second has to be a number.

    Returns:
        Union[int, float] -- the sum.
    """
    if not isinstance(first, (int, float)):
        raise TypeError('first has to be a number')
    if not isinstance(second, (int, float)):
        raise TypeError('second has to be a number')
    return first + second


def subtract(first: Union[int, float], second: Union[int, float]) -> Union[int, float]:
    """Subtract two numbers.

    Arguments:
        first {Union[int, float]} -- First number.
        second {Union[int, float]} -- second number.

    Raises:
        TypeError: first has to be a number.
        TypeError: second has to be a number.

    Returns:
        Union[int, float] -- the difference.
    """

    if not isinstance(first, (int, float)):
        raise TypeError('first has to be a number')
    if not isinstance(second, (int, float)):
        raise TypeError('second has to be a number')
    return first - second


if __name__ == "__main__":
    pass
