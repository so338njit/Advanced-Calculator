"""Division command implementation"""
from decimal import Decimal
from calculator.commands.command import Command

class DivideCommand(Command):
    """Command for division operation"""
    
    @property
    def name(self) -> str:
        """Name of the command"""
        return "divide"
    
    def execute(self) -> Decimal:
        """Perform division"""
        if self.b == 0:
            raise ValueError("Division by zero is not allowed")
        return self.a / self.b
    
    def __repr__(self):
        """String representation"""
        return f"DivideCommand({self.a}, {self.b})"
