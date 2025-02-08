from decimal import Decimal

@staticmethod
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

@staticmethod
def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

@staticmethod
def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Divide by zero not allowed")
    return a / b

@staticmethod
def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b
