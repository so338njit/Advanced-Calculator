# Import modules and classes
from decimal import Decimal
from typing import Callable
from calculator.calculations import Calculations
from calculator.operations import add, subtract, divide, multiply
from calculator.calculation import Calculation

# pylint: disable=invalid-name
# pylint: disable=line-to-long
# Definition of the calculator class
class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        #Creates and performs a calculation, then return the result
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        #create method for performing add by delegating to the perform_operation method
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        #create method for performing subtract by delegating to the perform_operation method
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        #create method for performing multiply by delegating to the perform_operation method
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        #create method for performing divide by delegating to the perform_operation method
        return Calculator._perform_operation(a, b, divide)
