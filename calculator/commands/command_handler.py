"""Command handler that executes commands and maintains history"""
import os
from typing import List
from calculator.commands.command import Command
from calculator.config import MAX_HISTORY_SIZE

class CommandHandler:
    """Handles the execution of commands and maintains history"""

    def __init__(self):
        """Initialize with empty history"""
        self.history: List[Command] = []
        self.max_history_size = MAX_HISTORY_SIZE

    def add_to_history(self, command):
        self.history.append(command)
        if len(self.history) > self.max_history_size:
            self.history = self.history[-self.max_history_size:]

    def execute(self, command: Command):
        """Execute a command and store it in history"""
        result = command.execute()
        self.add_to_history(command)
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
