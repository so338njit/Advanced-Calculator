"""configuration testing file"""
# pylint: disable=unused-import
import os
from unittest import mock
import pytest


def test_config_default_values():
    """Test that config uses default values when env vars are not set."""
    # Remove any existing env vars that might affect the test
    # pylint: disable=import-outside-toplevel
    with mock.patch.dict(os.environ, {}, clear=True):
        # Fresh import to ensure defaults are used
        import importlib
        import calculator.config
        importlib.reload(calculator.config)

        # Check default values
        assert calculator.config.MAX_HISTORY_SIZE == 100
        assert calculator.config.DECIMAL_PRECISION == 10
        # ... test other defaults

def test_config_uses_environment_variables():
    """Test that config uses values from environment variables."""
    # pylint: disable=import-outside-toplevel
    with mock.patch.dict(os.environ, {
        'MAX_HISTORY_SIZE': '50',
        'DECIMAL_PRECISION': '5'
    }):
        # Fresh import to pick up the mocked env vars
        import importlib
        import calculator.config
        importlib.reload(calculator.config)

        # Check values from env vars
        assert calculator.config.MAX_HISTORY_SIZE == 50
        assert calculator.config.DECIMAL_PRECISION == 5
        # ... test other configured values
