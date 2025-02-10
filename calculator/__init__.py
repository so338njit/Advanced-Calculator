"""Calculator module providing basic arithmetic operations.

This module implements a Calculator class that performs addition, subtraction,
multiplication, and division operations while maintaining a history of calculations.
"""
from decimal import Decimal
from typing import Callable
from calculator.calculations import Calculations
from calculator.operations import add, subtract, divide, multiply
from calculator.calculation import Calculation

# pylint: disable=invalid-name

class Calculator:
    """A calculator class that performs basic arithmetic"""
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Creates and performs a calculation, then return the result"""
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """add two numbers together"""
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """subtract the second number from the first"""
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """multiply two numbers"""
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Divide the first number by the second"""
        return Calculator._perform_operation(a, b, divide)
