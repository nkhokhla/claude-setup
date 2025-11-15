"""Data loading and processing utilities."""

from pathlib import Path
from typing import Optional

import pandas as pd


def load_dataset(
    file_path: str | Path,
    *,
    nrows: Optional[int] = None,
) -> pd.DataFrame:
    """Load dataset from CSV with validation.

    Args:
        file_path: Path to CSV file
        nrows: Optional limit on rows to load

    Returns:
        Loaded and validated DataFrame

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If data validation fails

    Example:
        >>> df = load_dataset("data.csv")
        >>> df = load_dataset("data.csv", nrows=1000)
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path, nrows=nrows)

    if df.empty:
        raise ValueError("Dataset is empty")

    return df


def clean_data(df: pd.DataFrame, *, drop_na: bool = True) -> pd.DataFrame:
    """Clean DataFrame by removing null values and duplicates.

    Args:
        df: DataFrame to clean
        drop_na: Whether to drop rows with null values

    Returns:
        Cleaned DataFrame

    Example:
        >>> df_clean = clean_data(df)
        >>> df_clean = clean_data(df, drop_na=False)
    """
    result = df.copy()

    if drop_na:
        result = result.dropna()

    result = result.drop_duplicates()

    return result
