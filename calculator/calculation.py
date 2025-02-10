"""Defining a class that encapsulates a mathematical calculation"""
# pylint: disable=unused-import
# pylint: disable=invalid-name
from decimal import Decimal
from typing import Callable
from calculator.operations import add, multiply, subtract, divide

# Definition of the calculator class
class Calculation:
    """ Constructor method"""
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """initialize a new Calculation instance."""
        self.a = a
        self.b = b
        self.operation = operation # stores the operation function for later recall

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Create a new Calculation instance using the factory pattern"""
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        '''execute the stored calculation and return the result'''
        return self.operation(self.a, self.b)

    def __repr__(self):
        '''retrun a string representation of the Calculation'''
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
