'''My Calculator Test'''
from calculator import add, subtract, divide, multiply

def test_addition():
    '''tests that the add function works'''
    assert add(2,2) == 4

def test_subtraction():
    '''tests that the subtract function works'''
    assert subtract(2,2) == 0

def test_divide():
    '''tests that the divide function works'''
    assert divide(2,2) == 1

def test_multiply():
    '''tests that the add function works'''
    assert multiply(2,2) == 4
