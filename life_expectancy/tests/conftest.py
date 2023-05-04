"""Pytest configuration file"""
import pandas as pd
import pytest

from .fixtures.mock import raw_data, expect_data
from . import FIXTURES_DIR

@pytest.fixture()
def goal_data_fixture():
    """Fixture with the goal of cleaning the raw_data()"""
    return pd.DataFrame(expect_data())

@pytest.fixture()
def source_data_fixture():
    """Fixture with the raw data defined in the mock file"""
    return pd.DataFrame(raw_data())

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")
