"""Tests for the base Command class."""
from decimal import Decimal
import pytest
from calculator.commands.command import Command


class ConcreteCommand(Command):
    """Concrete implementation of Command for testing."""

    @property
    def name(self) -> str:
        """Return the name of the command."""
        return "test_command"

    def execute(self) -> Decimal:
        """Execute the command implementation."""
        return self.a + self.b


def test_command_initialization(decimal_values):
    """Test that a Command can be initialized with two decimal values."""
    a, b = decimal_values['a'], decimal_values['b']
    cmd = ConcreteCommand(a, b)

    assert cmd.a == a
    assert cmd.b == b


def test_command_abstract_methods():
    """Test that Command is properly set up as an abstract class."""
    # Attempting to instantiate Command directly should raise TypeError
    with pytest.raises(TypeError):
        Command(Decimal('1'), Decimal('2')) # pylint: disable=abstract-class-instantiated


def test_concrete_command_name():
    """Test that a concrete command implementation has a name property."""
    cmd = ConcreteCommand(Decimal('1'), Decimal('2'))
    assert cmd.name == "test_command"


def test_concrete_command_execute(decimal_values):
    """Test that a concrete command can be executed."""
    a, b = decimal_values['a'], decimal_values['b']
    cmd = ConcreteCommand(a, b)

    result = cmd.execute()
    assert result == a + b
    assert isinstance(result, Decimal)
