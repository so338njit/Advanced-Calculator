"""Multiplication command implementation"""
from decimal import Decimal
from calculator.commands.command import Command

class MultiplyCommand(Command):
    """Command for multiplication operation"""
    
    @property
    def name(self) -> str:
        """Name of the command"""
        return "multiply"
    
    def execute(self) -> Decimal:
        """Perform multiplication"""
        return self.a * self.b
    
    def __repr__(self):
        """String representation"""
        return f"MultiplyCommand({self.a}, {self.b})"
