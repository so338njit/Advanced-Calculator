"""testing operations"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    """testing the addition opertion"""
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    assert calculation.perform() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    """testing the subtraction operation"""
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('5'), "Subtract operation failed"

def test_operation_multiply():
    """testing the multiplication operation"""
    calculation = Calculation(Decimal('2'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('10'), "Multiply operation failed"

def test_operation_divide():
    """testing the divide operation"""
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    """testing the exception to divide by zero"""
    with pytest.raises(ValueError, match="Divide by zero not allowed"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()