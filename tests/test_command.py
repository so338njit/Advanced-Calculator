"""Test module for Command implementations."""
from decimal import Decimal
import pytest
from calculator.commands.operations import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class TestAddCommand:
    """Test suite for the AddCommand class."""

    def test_execute(self):
        """Test the execute method."""
        cmd = AddCommand(Decimal('5'), Decimal('3'))
        result = cmd.execute()
        assert result == Decimal('8')

    def test_name(self):
        """Test the name property."""
        cmd = AddCommand(Decimal('5'), Decimal('3'))
        assert cmd.name == "add"

    def test_repr(self):
        """Test the string representation."""
        cmd = AddCommand(Decimal('5'), Decimal('3'))
        assert repr(cmd) == "AddCommand(5, 3)"

class TestSubtractCommand:
    """Test suite for the SubtractCommand class."""

    def test_execute(self):
        """Test the execute method."""
        cmd = SubtractCommand(Decimal('8'), Decimal('3'))
        result = cmd.execute()
        assert result == Decimal('5')

    def test_name(self):
        """Test the name property."""
        cmd = SubtractCommand(Decimal('8'), Decimal('3'))
        assert cmd.name == "subtract"

    def test_repr(self):
        """Test the string representation."""
        cmd = SubtractCommand(Decimal('8'), Decimal('3'))
        assert repr(cmd) == "SubtractCommand(8, 3)"

class TestMultiplyCommand:
    """Test suite for the MultiplyCommand class."""

    def test_execute(self):
        """Test the execute method."""
        cmd = MultiplyCommand(Decimal('4'), Decimal('3'))
        result = cmd.execute()
        assert result == Decimal('12')

    def test_name(self):
        """Test the name property."""
        cmd = MultiplyCommand(Decimal('4'), Decimal('3'))
        assert cmd.name == "multiply"

    def test_repr(self):
        """Test the string representation."""
        cmd = MultiplyCommand(Decimal('4'), Decimal('3'))
        assert repr(cmd) == "MultiplyCommand(4, 3)"

class TestDivideCommand:
    """Test suite for the DivideCommand class."""

    def test_execute(self):
        """Test the execute method."""
        cmd = DivideCommand(Decimal('12'), Decimal('4'))
        result = cmd.execute()
        assert result == Decimal('3')

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        cmd = DivideCommand(Decimal('12'), Decimal('0'))
        with pytest.raises(ValueError) as exc_info:
            cmd.execute()
        assert "Division by zero is not allowed" in str(exc_info.value)

    def test_name(self):
        """Test the name property."""
        cmd = DivideCommand(Decimal('12'), Decimal('4'))
        assert cmd.name == "divide"

    def test_repr(self):
        """Test the string representation."""
        cmd = DivideCommand(Decimal('12'), Decimal('4'))
        assert repr(cmd) == "DivideCommand(12, 4)"
