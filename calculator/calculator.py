"""Calculator module providing basic arithmetic operations.

This module implements a Calculator class that performs addition, subtraction,
multiplication, and division operations while maintaining a history of calculations.
"""
from decimal import Decimal
from calculator.commands import CommandHandler
from calculator.commands.operations import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class Calculator:
    """A calculator class that performs basic arithmetic using the command pattern"""

    def __init__(self):
        """Initialize calculator with a command handler"""
        self.command_handler = CommandHandler()

    def add(self, a: Decimal, b: Decimal) -> Decimal:
        """Add two numbers together"""
        command = AddCommand(a, b)
        return self.command_handler.execute(command)

    def subtract(self, a: Decimal, b: Decimal) -> Decimal:
        """Subtract the second number from the first"""
        command = SubtractCommand(a, b)
        return self.command_handler.execute(command)

    def multiply(self, a: Decimal, b: Decimal) -> Decimal:
        """Multiply two numbers"""
        command = MultiplyCommand(a, b)
        return self.command_handler.execute(command)

    def divide(self, a: Decimal, b: Decimal) -> Decimal:
        """Divide the first number by the second"""
        command = DivideCommand(a, b)
        return self.command_handler.execute(command)

    def get_history(self):
        """Return the calculation history"""
        return self.command_handler.get_history()
