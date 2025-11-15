"""Visualization utilities for data analysis."""

from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_distribution(
    data: pd.Series,
    title: Optional[str] = None,
    **kwargs: object,
) -> plt.Figure:
    """Plot distribution with KDE overlay.

    Args:
        data: Series to plot
        title: Optional plot title
        **kwargs: Additional arguments for seaborn histplot

    Returns:
        Matplotlib figure

    Example:
        >>> fig = plot_distribution(df['age'], title='Age Distribution')
        >>> fig.savefig('age_dist.png')
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data, kde=True, ax=ax, **kwargs)

    if title:
        ax.set_title(title)

    ax.set_xlabel(data.name or "Value")
    ax.set_ylabel("Frequency")

    return fig


def plot_correlation_matrix(df: pd.DataFrame, **kwargs: object) -> plt.Figure:
    """Plot correlation matrix heatmap.

    Args:
        df: DataFrame with numeric columns
        **kwargs: Additional arguments for seaborn heatmap

    Returns:
        Matplotlib figure

    Example:
        >>> fig = plot_correlation_matrix(df)
        >>> fig.savefig('correlation.png')
    """
    fig, ax = plt.subplots(figsize=(12, 10))

    corr = df.corr()
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        ax=ax,
        **kwargs,
    )

    ax.set_title("Correlation Matrix")

    return fig
