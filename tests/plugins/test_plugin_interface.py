"""Tests for the PluginInterface class."""
from decimal import Decimal
from typing import Type
import pytest
from calculator.commands.command import Command
from calculator.plugins.plugin_interface import PluginInterface


class SampleCommand(Command):
    """Test command for plugin interface testing."""

    @property
    def name(self) -> str:
        """Return command name."""
        return "test_command"

    def execute(self) -> Decimal:
        """Execute the command."""
        return self.a + self.b


class ConcretePlugin(PluginInterface):
    """Concrete implementation of PluginInterface for testing."""

    @classmethod
    def get_name(cls) -> str:
        """Return the plugin name."""
        return "test_plugin"

    @classmethod
    def get_plugin_type(cls) -> str:
        """Return the plugin type."""
        return "test_type"

    @classmethod
    def get_command_class(cls) -> Type[Command]:
        """Return the command class."""
        return SampleCommand


def test_plugin_interface_abstract():
    """Test that PluginInterface is properly abstract."""
    # Should not be able to instantiate directly
    with pytest.raises(TypeError):
        PluginInterface() # pylint: disable=abstract-class-instantiated


def test_concrete_plugin():
    """Test a concrete implementation of PluginInterface."""
    # Should be able to access class methods
    assert ConcretePlugin.get_name() == "test_plugin"
    assert ConcretePlugin.get_plugin_type() == "test_type"
    assert ConcretePlugin.get_command_class() == SampleCommand


def test_plugin_command_instantiation():
    """Test that the command class from a plugin can be instantiated."""
    command_class = ConcretePlugin.get_command_class()
    cmd = command_class(Decimal('5'), Decimal('10'))

    assert cmd.name == "test_command"
    assert cmd.execute() == Decimal('15')
