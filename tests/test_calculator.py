"""Tests for the Calculator class."""
# pylint: disable=unused-import, protected-access, no-member
from decimal import Decimal
from unittest.mock import patch, MagicMock
import pytest
from calculator.calculator import Calculator
from calculator.commands import CommandHandler
from calculator.plugins import get_plugin_manager
from calculator.plugins.plugin_interface import PluginInterface


class MockPlugin(PluginInterface):
    """Mock plugin for testing."""

    @classmethod
    def get_name(cls):
        """Return plugin name."""
        return "mock_operation"

    @classmethod
    def get_plugin_type(cls):
        """Return plugin type."""
        return "operation"

    @classmethod
    def get_command_class(cls):
        """Return command class."""
        return MagicMock


# This is the key fix - patch the correct module path
@patch('calculator.calculator.get_plugin_manager')
def test_calculator_initialization(mock_get_plugin_manager):
    """Test initializing a Calculator."""
    # Create a mock plugin manager
    mock_plugin_manager = MagicMock()
    mock_plugin_manager.get_plugins.return_value = {}

    # Set up the mock plugin manager
    mock_get_plugin_manager.return_value = mock_plugin_manager

    # Create a calculator
    calc = Calculator()

    # Verify the calculator was initialized correctly
    assert isinstance(calc.command_handler, CommandHandler)
    assert calc.plugin_manager == mock_plugin_manager

    # Verify discover_plugins was called
    mock_plugin_manager.discover_plugins.assert_called_once_with("calculator.plugins.operations")

    # Verify get_plugins was called
    mock_plugin_manager.get_plugins.assert_called_with("operation")


@patch('calculator.calculator.get_plugin_manager')
def test_calculator_create_operation_methods(mock_get_plugin_manager):
    """Test creating operation methods."""
    # Create a mock plugin class
    mock_op_plugin = MagicMock()
    mock_op_plugin.get_name.return_value = "mock_operation"
    mock_op_plugin.get_plugin_type.return_value = "operation"
    mock_op_plugin.get_command_class.return_value = MagicMock()

    # Create a mock plugin manager
    mock_plugin_manager = MagicMock()
    mock_plugin_manager.get_plugins.return_value = {"mock_operation": mock_op_plugin}

    # Set up the mock plugin manager
    mock_get_plugin_manager.return_value = mock_plugin_manager

    # Create a calculator
    calc = Calculator()

    # Verify the mock_operation method was created
    assert hasattr(calc, "mock_operation")

    # Check the method documentation
    assert "Perform the mock_operation operation" in calc.mock_operation.__doc__


@patch('calculator.calculator.get_plugin_manager')
def test_calculator_operation_method(mock_get_plugin_manager):
    """Test using an operation method."""
    # Create a mock command class
    mock_command = MagicMock()
    mock_command.return_value.execute.return_value = Decimal('15')

    # Create a mock plugin class
    mock_op_plugin = MagicMock()
    mock_op_plugin.get_name.return_value = "test_op"
    mock_op_plugin.get_plugin_type.return_value = "operation"
    mock_op_plugin.get_command_class.return_value = mock_command

    # Create a mock plugin manager
    mock_plugin_manager = MagicMock()
    mock_plugin_manager.get_plugins.return_value = {"test_op": mock_op_plugin}

    # Set up the mock plugin manager
    mock_get_plugin_manager.return_value = mock_plugin_manager

    # Create a calculator
    calc = Calculator()

    # Call the operation method
    result = calc.test_op(Decimal('10'), Decimal('5'))

    # Verify the command was created and executed
    mock_command.assert_called_once_with(Decimal('10'), Decimal('5'))
    mock_command.return_value.execute.assert_called_once()
    assert result == Decimal('15')


@patch('calculator.calculator.get_plugin_manager')
def test_calculator_get_available_operations(mock_get_plugin_manager):
    """Test getting available operations."""
    # Create a mock plugin class
    mock_op_plugin = MagicMock()
    mock_op_plugin.get_name.return_value = "test_op"
    mock_op_plugin.get_plugin_type.return_value = "operation"

    # Create a mock plugin manager
    mock_plugin_manager = MagicMock()
    mock_plugin_manager.get_plugins.return_value = {"test_op": mock_op_plugin}

    # Set up the mock plugin manager
    mock_get_plugin_manager.return_value = mock_plugin_manager

    # Create a calculator
    calc = Calculator()

    # Get available operations
    ops = calc.get_available_operations()

    # Verify the result
    assert ops == {"test_op": "operation"}


@patch('calculator.calculator.get_plugin_manager')
def test_calculator_get_history(mock_get_plugin_manager):
    """Test getting the calculation history."""
    # Create a mock plugin manager
    mock_plugin_manager = MagicMock()
    mock_plugin_manager.get_plugins.return_value = {}

    # Set up the mock plugin manager
    mock_get_plugin_manager.return_value = mock_plugin_manager

    # Create a calculator
    calc = Calculator()

    # Set up a mock command handler
    calc.command_handler = MagicMock()
    mock_history = [MagicMock(), MagicMock()]
    calc.command_handler.get_history.return_value = mock_history

    # Get history
    history = calc.get_history()

    # Verify the result
    assert history == mock_history
    calc.command_handler.get_history.assert_called_once()


@patch('calculator.calculator.get_plugin_manager')
def test_calculator_reload_plugins(mock_get_plugin_manager):
    """Test reloading plugins."""
    # Create a mock plugin class
    mock_op_plugin = MagicMock()
    mock_op_plugin.get_name.return_value = "mock_operation"
    mock_op_plugin.get_plugin_type.return_value = "operation"
    mock_op_plugin.get_command_class.return_value = MagicMock()

    # Create a mock plugin manager
    mock_plugin_manager = MagicMock()
    mock_plugin_manager.get_plugins.return_value = {"mock_operation": mock_op_plugin}

    # Set up the mock plugin manager
    mock_get_plugin_manager.return_value = mock_plugin_manager

    # Create a calculator
    calc = Calculator()

    # Clear the method cache
    calc._method_cache = {}

    # Reload plugins
    calc.reload_plugins()

    # Verify discover_plugins was called
    mock_plugin_manager.discover_plugins.assert_called_with("calculator.plugins.operations")

    # Verify get_plugins was called
    mock_plugin_manager.get_plugins.assert_called_with("operation")

    # Verify methods were created
    assert "mock_operation" in calc._method_cache


def test_calculator_integration():
    """Integration test for the Calculator with real plugins."""
    # Create a calculator with the real plugin system
    calc = Calculator()

    # Test the add operation
    result = calc.add(Decimal('10'), Decimal('5'))
    assert result == Decimal('15')

    # Test the subtract operation
    result = calc.subtract(Decimal('10'), Decimal('5'))
    assert result == Decimal('5')

    # Test the multiply operation
    result = calc.multiply(Decimal('10'), Decimal('5'))
    assert result == Decimal('50')

    # Test the divide operation
    result = calc.divide(Decimal('10'), Decimal('5'))
    assert result == Decimal('2')

    # Verify operations are dynamically loaded
    available_ops = calc.get_available_operations()
    assert "add" in available_ops
    assert "subtract" in available_ops
    assert "multiply" in available_ops
    assert "divide" in available_ops

    # Check history
    history = calc.get_history()
    assert len(history) == 4
    assert history[0].name == "add"
    assert history[1].name == "subtract"
    assert history[2].name == "multiply"
    assert history[3].name == "divide"
