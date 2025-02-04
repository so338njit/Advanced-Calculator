from calculator.calculation import Calculation
from calculator.operations import add, subtract, divide, multiply

class Calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculation(a, b, add) #pass the add function from operations
        return calculation.get_result()
    
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a, b, subtract) #pass the subtract function from operation
        return calculation.get_result()
    
    @staticmethod
    def multiply(a,b):
        calculation = Calculation(a, b, multiply) #pass the multiply function from operation
        return calculation.get_result()
    
    @staticmethod
    def divide(a,b):
        calculation = Calculation(a, b, divide) #pass the miltiply function from operation
        return calculation.get_result()
    