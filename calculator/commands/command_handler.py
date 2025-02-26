"""Command handler that executes commands and maintains history"""
from typing import List
from calculator.commands.command import Command

class CommandHandler:
    """Handles the execution of commands and maintains history"""

    def __init__(self):
        """Initialize with empty history"""
        self.history: List[Command] = []

    def execute(self, command: Command):
        """Execute a command and store it in history"""
        result = command.execute()
        self.history.append(command)
        return result

    def get_history(self) -> List[Command]:
        """Return the command history"""
        return self.history

    def clear_history(self):
        """Clear the command history"""
        self.history.clear()

    def get_latest(self):
        """Get the most recent command"""
        if self.history:
            return self.history[-1]
        return None

    def find_by_command_name(self, name: str) -> List[Command]:
        """Find commands by name"""
        return [cmd for cmd in self.history if cmd.name == name]
