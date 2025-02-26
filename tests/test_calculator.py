"""Test module for the Calculator class."""
from decimal import Decimal
import pytest
from calculator import Calculator

class TestCalculator:
    """Test suite for the Calculator class."""

# pylint: disable=attribute-defined-outside-init
    def setup_method(self):
        """Set up test fixture."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition functionality."""
        # Test positive numbers
        result = self.calc.add(Decimal('5'), Decimal('3'))
        assert result == Decimal('8')

        # Test negative numbers
        result = self.calc.add(Decimal('-5'), Decimal('3'))
        assert result == Decimal('-2')

        # Test decimals
        result = self.calc.add(Decimal('5.5'), Decimal('3.3'))
        assert result == Decimal('8.8')

        # Test zero
        result = self.calc.add(Decimal('0'), Decimal('3'))
        assert result == Decimal('3')

    def test_subtract(self):
        """Test subtraction functionality."""
        # Test positive result
        result = self.calc.subtract(Decimal('8'), Decimal('3'))
        assert result == Decimal('5')

        # Test negative result
        result = self.calc.subtract(Decimal('3'), Decimal('8'))
        assert result == Decimal('-5')

        # Test with zero
        result = self.calc.subtract(Decimal('8'), Decimal('0'))
        assert result == Decimal('8')

        # Test decimals
        result = self.calc.subtract(Decimal('8.5'), Decimal('3.2'))
        assert result == Decimal('5.3')

    def test_multiply(self):
        """Test multiplication functionality."""
        # Test positive numbers
        result = self.calc.multiply(Decimal('4'), Decimal('3'))
        assert result == Decimal('12')

        # Test with zero
        result = self.calc.multiply(Decimal('4'), Decimal('0'))
        assert result == Decimal('0')

        # Test negative numbers
        result = self.calc.multiply(Decimal('-4'), Decimal('3'))
        assert result == Decimal('-12')

        # Test decimals
        result = self.calc.multiply(Decimal('4.5'), Decimal('2.5'))
        assert result == Decimal('11.25')

    def test_divide(self):
        """Test division functionality."""
        # Test even division
        result = self.calc.divide(Decimal('12'), Decimal('4'))
        assert result == Decimal('3')

        # Test division with remainder
        result = self.calc.divide(Decimal('10'), Decimal('3'))
        assert result == Decimal('10') / Decimal('3')

        # Test division by negative
        result = self.calc.divide(Decimal('12'), Decimal('-4'))
        assert result == Decimal('-3')

        # Test division of zero
        result = self.calc.divide(Decimal('0'), Decimal('5'))
        assert result == Decimal('0')

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError) as exc_info:
            self.calc.divide(Decimal('10'), Decimal('0'))
        assert "Division by zero is not allowed" in str(exc_info.value)

    def test_history(self):
        """Test history functionality."""
        # Perform some calculations
        self.calc.add(Decimal('5'), Decimal('3'))
        self.calc.subtract(Decimal('10'), Decimal('4'))
        self.calc.multiply(Decimal('3'), Decimal('6'))

        # Check history
        history = self.calc.get_history()
        assert len(history) == 3
        assert history[0].name == "add"
        assert history[1].name == "subtract"
        assert history[2].name == "multiply"
