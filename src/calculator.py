"""
Calculator module providing basic arithmetic operations.
"""

def add(num1, num2):
    """
    Add two numbers and return the result.

    Args:
        num1 (int or float): First number
        num2 (int or float): Second number

    Returns:
        int or float: Sum of num1 and num2
    """
    return num1 + num2


def subtract(minuend, subtrahend):
    """
    Subtract one number from another and return the result.

    Args:
        minuend (int or float): The number to subtract from
        subtrahend (int or float): The number to subtract

    Returns:
        int or float: Difference between minuend and subtrahend
    """
    return minuend - subtrahend


def multiply(factor1, factor2):
    """
    Multiply two numbers and return the result.

    Args:
        factor1 (int or float): The first number to multiply
        factor2 (int or float): The second number to multiply

    Returns:
        int or float: Product of factor1 and factor2
    """
    return factor1 * factor2


def divide(dividend, divisor):
    """
    Divide one number by another and return the result.

    Args:
        dividend (int or float): The number to be divided
        divisor (int or float): The number by which to divide

    Returns:
        float: Quotient of dividend divided by divisor

    Raises:
        ValueError: If divisor is zero, since division by zero is not allowed
    """
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    return dividend / divisor
