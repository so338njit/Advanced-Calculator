"""Module testing the calculation.py file"""
# pylint: disable=unnecessary-dunder-call, invalid-name, unused-import
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_operations(a, b, operation, expected):
    """Test calculation operations"""
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operations with {a} and {b}"

def test_calculation_repr():
    """Test string representation of Calculation objects"""
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zreo():
    """Test that division by zero raises appropriate error"""
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Divide by zero not allowed"):
        calc.perform()
