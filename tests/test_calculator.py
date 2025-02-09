'''My Calculator Test'''
from calculator import Calculator
def test_addition():
    '''tests that the add function works'''
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''tests that the subtract function works'''
    assert Calculator.subtract(2,2) == 0

def test_divide():
    '''tests that the divide function works'''
    assert Calculator.divide(2,2) == 1

def test_multiply():
    '''tests that the multiply function works'''
    assert Calculator.multiply(2,2) == 4
