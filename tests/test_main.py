"""Test module for the main CLI interface."""
# pylint: disable=unused-import
from decimal import Decimal
from io import StringIO
import sys
from unittest.mock import patch
import pytest
import main
from calculator import Calculator

# pylint: disable=too-many-public-methods
class TestMain:
    """Test suite for the main CLI interface."""
# pylint: disable=attribute-defined-outside-init

    def setup_method(self):
        """Set up test fixture."""
        self.calc = Calculator()

    @patch('sys.stdout', new_callable=StringIO)
    def test_process_command_add(self, mock_stdout):
        """Test processing an add command."""
        main.process_command(self.calc, ["4", "3", "add"])
        assert "4 + 3 = 7" in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_process_command_subtract(self, mock_stdout):
        """Test processing a subtract command."""
        main.process_command(self.calc, ["10", "3", "subtract"])
        assert "10 - 3 = 7" in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_process_command_multiply(self, mock_stdout):
        """Test processing a multiply command."""
        main.process_command(self.calc, ["4", "3", "multiply"])
        assert "4 * 3 = 12" in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_process_command_divide(self, mock_stdout):
        """Test processing a divide command."""
        main.process_command(self.calc, ["12", "3", "divide"])
        assert "12 / 3 = 4" in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_process_command_invalid_operation(self, mock_stdout):
        """Test processing an invalid operation."""
        main.process_command(self.calc, ["4", "3", "power"])
        assert "Error: Unknown operation 'power'" in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_process_command_invalid_args_count(self, mock_stdout):
        """Test processing a command with incorrect number of arguments."""
        main.process_command(self.calc, ["4", "add"])
        assert "Error: Commands must have exactly 3 parts" in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_process_command_invalid_number(self, mock_stdout):
        """Test processing a command with invalid numbers."""
        main.process_command(self.calc, ["four", "3", "add"])
        assert "Error: Operands must be valid numbers" in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_process_command_divide_by_zero(self, mock_stdout):
        """Test processing a divide by zero command."""
        main.process_command(self.calc, ["4", "0", "divide"])
        assert "Error: Division by zero is not allowed" in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_help(self, mock_stdout):
        """Test the print_help function."""
        main.print_help()
        output = mock_stdout.getvalue()
        assert "Advanced Calculator" in output
        assert "Usage:" in output
        assert "Commands:" in output

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_history_empty(self, mock_stdout):
        """Test showing empty history."""
        main.show_history(self.calc)
        assert "No calculations in history" in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_history_with_commands(self, mock_stdout):
        """Test showing history with commands."""
        # Add some commands to history
        self.calc.add(Decimal('5'), Decimal('3'))
        self.calc.subtract(Decimal('10'), Decimal('4'))

        main.show_history(self.calc)
        output = mock_stdout.getvalue()
        assert "Calculation History:" in output
        assert "1." in output
        assert "2." in output

    @patch('builtins.input', side_effect=["4 3 add", "exit"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_interactive_mode(self, mock_stdout, mock_input):
        """Test the interactive mode of the main function."""
        with patch.object(sys, 'argv', ['main.py']):
            main.main()

        output = mock_stdout.getvalue()
        assert "Advanced Calculator - Interactive Mode" in output
        assert "4 + 3 = 7" in output

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_command_args(self, mock_stdout):
        """Test the main function with command arguments."""
        with patch.object(sys, 'argv', ['main.py', '5', '2', 'multiply']):
            main.main()

        assert "5 * 2 = 10" in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_help_arg(self, mock_stdout):
        """Test the main function with help argument."""
        with patch.object(sys, 'argv', ['main.py', 'help']):
            main.main()

        assert "Advanced Calculator - Command Line Interface" in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_history_arg(self, mock_stdout):
        """Test the main function with history argument."""
        with patch.object(sys, 'argv', ['main.py', 'history']):
            main.main()

        assert "No calculations in history" in mock_stdout.getvalue()

    @patch('builtins.input', side_effect=["invalid command", "exit"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_interactive_invalid_command(self, mock_stdout, mock_input):
        """Test handling invalid commands in interactive mode."""
        with patch.object(sys, 'argv', ['main.py']):
            main.main()

        assert "Error: Commands must have exactly 3 parts" in mock_stdout.getvalue()

    @patch('builtins.input', side_effect=KeyboardInterrupt)
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_interactive_keyboard_interrupt(self, mock_stdout, mock_input):
        """Test handling keyboard interrupt in interactive mode."""
        with patch.object(sys, 'argv', ['main.py']):
            main.main()

        assert "Exiting..." in mock_stdout.getvalue()

    @patch('builtins.input', side_effect=["help", "exit"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_interactive_help(self, mock_stdout, mock_input):
        """Test help command in interactive mode."""
        with patch.object(sys, 'argv', ['main.py']):
            main.main()

        assert "Advanced Calculator - Command Line Interface" in mock_stdout.getvalue()

    @patch('builtins.input', side_effect=["history", "exit"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_interactive_history(self, mock_stdout, mock_input):
        """Test history command in interactive mode."""
        with patch.object(sys, 'argv', ['main.py']):
            main.main()

        assert "No calculations in history" in mock_stdout.getvalue()

    @patch('builtins.input', side_effect=["", "exit"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_interactive_empty_input(self, mock_stdout, mock_input):
        """Test empty input in interactive mode."""
        with patch.object(sys, 'argv', ['main.py']):
            main.main()

        # Empty input should not produce an error
        assert "Error:" not in mock_stdout.getvalue()
