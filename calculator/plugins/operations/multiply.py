"""Multiplication operation plugin."""
from decimal import Decimal
from typing import Type

from calculator.commands.command import Command
from calculator.plugins.plugin_interface import PluginInterface


class MultiplyCommand(Command):
    """Command for multiplication operation."""

    @property
    def name(self) -> str:
        """Name of the command."""
        return "multiply"

    def execute(self) -> Decimal:
        """Perform multiplication."""
        return self.a * self.b

    def __repr__(self):
        """String representation."""
        return f"MultiplyCommand({self.a}, {self.b})"


class MultiplyPlugin(PluginInterface):
    """Plugin for multiplication operation."""

    @classmethod
    def get_name(cls) -> str:
        """Return the name of the plugin."""
        return "multiply"

    @classmethod
    def get_plugin_type(cls) -> str:
        """Return the type of the plugin."""
        return "operation"

    @classmethod
    def get_command_class(cls) -> Type[Command]:
        """Return the command class for this operation."""
        return MultiplyCommand
