"""Division operation plugin."""
from decimal import Decimal
from typing import Type

from calculator.commands.command import Command
from calculator.plugins.plugin_interface import PluginInterface


class DivideCommand(Command):
    """Command for division operation."""

    @property
    def name(self) -> str:
        """Name of the command."""
        return "divide"

    def execute(self) -> Decimal:
        """Perform division."""
        if self.b == 0:
            raise ValueError("Division by zero is not allowed")
        return self.a / self.b

    def __repr__(self):
        """String representation."""
        return f"DivideCommand({self.a}, {self.b})"


class DividePlugin(PluginInterface):
    """Plugin for division operation."""

    @classmethod
    def get_name(cls) -> str:
        """Return the name of the plugin."""
        return "divide"

    @classmethod
    def get_plugin_type(cls) -> str:
        """Return the type of the plugin."""
        return "operation"

    @classmethod
    def get_command_class(cls) -> Type[Command]:
        """Return the command class for this operation."""
        return DivideCommand
