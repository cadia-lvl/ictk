"""Placed here for pytest to construct it's path."""
import pytest


@pytest.fixture()
def igc_test_file():
    """Return the location of the test file."""
    return "./tests/igc_test_file.txt"


@pytest.fixture()
def bin_test_file():
    """Return the location of the test file."""
    return "./tests/bin_test_file.csv"