"""testing operations"""
# pylint: disable = unused-import, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation(a, b, operation, expected):
    """test covering all operations"""
    calculation = Calculation.create(a, b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    """testing the exception to divide by zero"""
    with pytest.raises(ValueError, match="Divide by zero not allowed"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
