"""Module for managing calculation history"""
# pylint: disable=unused-import
from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculations:
    """Class that maintains and provides access to calculation history"""

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add calculation to history"""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Gets full history of calculations"""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clears all calculations from history"""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Gets most recent calculation"""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Finds calculation by operation name"""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
