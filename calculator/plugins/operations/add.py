"""Addition operation plugin."""
from decimal import Decimal
from typing import Type

from calculator.commands.command import Command
from calculator.plugins.plugin_interface import PluginInterface


class AddCommand(Command):
    """Command for addition operation."""

    @property
    def name(self) -> str:
        """Name of the command."""
        return "add"

    def execute(self) -> Decimal:
        """Perform addition."""
        return self.a + self.b

    def __repr__(self):
        """String representation."""
        return f"AddCommand({self.a}, {self.b})"


class AddPlugin(PluginInterface):
    """Plugin for addition operation."""

    @classmethod
    def get_name(cls) -> str:
        """Return the name of the plugin."""
        return "add"

    @classmethod
    def get_plugin_type(cls) -> str:
        """Return the type of the plugin."""
        return "operation"

    @classmethod
    def get_command_class(cls) -> Type[Command]:
        """Return the command class for this operation."""
        return AddCommand
