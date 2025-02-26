"""Test module for the CommandHandler class."""
# pylint: disable=unused-import
from decimal import Decimal
from calculator.commands.command_handler import CommandHandler
from calculator.commands.operations import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class TestCommandHandler:
    """Test suite for the CommandHandler class."""

# pylint: disable=attribute-defined-outside-init
    def setup_method(self):
        """Set up test fixture."""
        self.handler = CommandHandler()

    def test_execute(self):
        """Test the execute method."""
        cmd = AddCommand(Decimal('5'), Decimal('3'))
        result = self.handler.execute(cmd)
        assert result == Decimal('8')
        assert len(self.handler.history) == 1
        assert self.handler.history[0] == cmd

    def test_get_history(self):
        """Test the get_history method."""
        cmd1 = AddCommand(Decimal('5'), Decimal('3'))
        cmd2 = SubtractCommand(Decimal('10'), Decimal('4'))
        self.handler.execute(cmd1)
        self.handler.execute(cmd2)

        history = self.handler.get_history()
        assert len(history) == 2
        assert history[0] == cmd1
        assert history[1] == cmd2

    def test_clear_history(self):
        """Test the clear_history method."""
        cmd = AddCommand(Decimal('5'), Decimal('3'))
        self.handler.execute(cmd)
        assert len(self.handler.get_history()) == 1

        self.handler.clear_history()
        assert len(self.handler.get_history()) == 0

    def test_get_latest(self):
        """Test the get_latest method."""
        # Test with empty history
        assert self.handler.get_latest() is None

        # Test with some commands
        cmd1 = AddCommand(Decimal('5'), Decimal('3'))
        cmd2 = SubtractCommand(Decimal('10'), Decimal('4'))
        self.handler.execute(cmd1)
        self.handler.execute(cmd2)

        latest = self.handler.get_latest()
        assert latest == cmd2

    def test_find_by_command_name(self):
        """Test the find_by_command_name method."""
        # Add some commands
        add_cmd = AddCommand(Decimal('5'), Decimal('3'))
        sub_cmd = SubtractCommand(Decimal('10'), Decimal('4'))
        mul_cmd = MultiplyCommand(Decimal('3'), Decimal('6'))
        add_cmd2 = AddCommand(Decimal('7'), Decimal('2'))

        self.handler.execute(add_cmd)
        self.handler.execute(sub_cmd)
        self.handler.execute(mul_cmd)
        self.handler.execute(add_cmd2)

        # Find commands by name
        add_commands = self.handler.find_by_command_name("add")
        assert len(add_commands) == 2
        assert add_cmd in add_commands
        assert add_cmd2 in add_commands

        # Find commands by name (single result)
        mul_commands = self.handler.find_by_command_name("multiply")
        assert len(mul_commands) == 1
        assert mul_cmd in mul_commands

        # Find commands by name (no results)
        div_commands = self.handler.find_by_command_name("divide")
        assert len(div_commands) == 0
