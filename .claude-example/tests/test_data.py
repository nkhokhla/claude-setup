"""Tests for data module."""

import pandas as pd
import pytest

from analysis.data import clean_data, load_dataset


def test_clean_data_removes_nulls() -> None:
    """Test that clean_data removes null values."""
    df = pd.DataFrame({"a": [1, None, 3], "b": [4, 5, None]})
    cleaned = clean_data(df)
    assert cleaned.isnull().sum().sum() == 0


def test_clean_data_removes_duplicates() -> None:
    """Test that clean_data removes duplicate rows."""
    df = pd.DataFrame({"a": [1, 2, 1], "b": [3, 4, 3]})
    cleaned = clean_data(df)
    assert len(cleaned) == 2


def test_clean_data_preserves_nulls_when_requested() -> None:
    """Test that clean_data preserves nulls when drop_na=False."""
    df = pd.DataFrame({"a": [1, None, 3], "b": [4, 5, 6]})
    cleaned = clean_data(df, drop_na=False)
    assert cleaned.isnull().sum().sum() > 0


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """Provide sample DataFrame for tests."""
    return pd.DataFrame(
        {
            "value": [1, 2, 3, 4, 5],
            "category": ["A", "B", "A", "B", "A"],
        }
    )


def test_sample_fixture_structure(sample_dataframe: pd.DataFrame) -> None:
    """Test that fixture provides expected structure."""
    assert len(sample_dataframe) == 5
    assert list(sample_dataframe.columns) == ["value", "category"]
