from calculator.calculations import Calculations
from calculator.operations import add, subtract, divide, multiply
from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        Calulations.add_calculation(calculation)
        return calculation.perform()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, Math.add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, Math.subtract)
    
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, Math.multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, Math.divide)
        