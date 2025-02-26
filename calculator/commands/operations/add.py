"""Addition command implementation"""
from decimal import Decimal
from calculator.commands.command import Command

class AddCommand(Command):
    """Command for addition operation"""

    @property
    def name(self) -> str:
        """Name of the command"""
        return "add"

    def execute(self) -> Decimal:
        """Perform addition"""
        return self.a + self.b

    def __repr__(self):
        """String representation"""
        return f"AddCommand({self.a}, {self.b})"
