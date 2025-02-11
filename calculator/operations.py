"""Module for returning arithmetic"""
# pylint: disable=invalid-name
from decimal import Decimal

@staticmethod
def add(a: Decimal, b: Decimal) -> Decimal:
    """function for returning addition"""
    return a + b

@staticmethod
def subtract(a: Decimal, b: Decimal) -> Decimal:
    """function for returning subtraction"""
    return a - b

@staticmethod
def divide(a: Decimal, b: Decimal) -> Decimal:
    """function for returning division"""
    if b == 0:
        raise ValueError("Divide by zero not allowed")
    return a / b

@staticmethod
def multiply(a: Decimal, b: Decimal) -> Decimal:
    """function for returning multiplication"""
    return a * b
