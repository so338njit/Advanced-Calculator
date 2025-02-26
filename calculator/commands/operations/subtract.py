"""Subtraction command implementation"""
from decimal import Decimal
from calculator.commands.command import Command

class SubtractCommand(Command):
    """Command for subtraction operation"""

    @property
    def name(self) -> str:
        """Name of the command"""
        return "subtract"

    def execute(self) -> Decimal:
        """Perform subtraction"""
        return self.a - self.b

    def __repr__(self):
        """String representation"""
        return f"SubtractCommand({self.a}, {self.b})"
