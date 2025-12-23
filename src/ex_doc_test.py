def sum(a, b):
    """
    Suma dos números.

    >>> sum(5, 7)
    12
    >>> sum(4, -4)
    0
    >>> sum(0, 0)
    0
    >>> sum(-3, -2)
    -5
    >>> sum(1.5, 2.5)
    4.0
    >>> sum("a", "b")
    'ab'
    >>> sum([1], [2])
    [1, 2]
    """
    return a + b


def subtract(a, b):
    """
    Resta dos números.

    >>> subtract(10, 5)
    5
    >>> subtract(0, 0)
    0
    >>> subtract(-5, -3)
    -2
    >>> subtract(2.5, 1.0)
    1.5
    >>> subtract("a", "b")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for -: 'str' and 'str'
    """
    return a - b


def multiply(a, b):
    """
    Multiplica dos valores.

    >>> multiply(3, 4)
    12
    >>> multiply(-2, 5)
    -10
    >>> multiply(0, 100)
    0
    >>> multiply(2.5, 2)
    5.0
    >>> multiply("a", 3)
    'aaa'
    >>> multiply([1], 2)
    [1, 1]
    >>> multiply("a", "b")
    Traceback (most recent call last):
        ...
    TypeError: can't multiply sequence by non-int of type 'str'
    """
    return a * b


def divide(a, b):
    """
    Divide dos números. Lanza error si el divisor es cero.

    >>> divide(10, 2)
    5.0
    >>> divide(5, 2)
    2.5
    >>> divide(-6, 3)
    -2.0
    >>> divide(0, 5)
    0.0
    >>> divide(10, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero
    >>> divide("a", 1)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for /: 'str' and 'int'
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # python -m doctest .\src\ex_doc_test.py
