"""
Basic unit tests for the Statistics Superstars project.
Run with: pytest tests/
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
from pathlib import Path
from src.data_loader import DataLoader


def test_cleaned_data_exists():
    """Check that the cleaned data file exists."""
    path = Path(__file__).parent.parent / "data" / "processed" / "cleaned_data.csv"
    assert path.exists(), "cleaned_data.csv should exist"


def test_cleaned_data_shape():
    """Check that cleaned data has the expected shape (149 rows, 7 columns)."""
    path = Path(__file__).parent.parent / "data" / "processed" / "cleaned_data.csv"
    df = pd.read_csv(path)
    assert df.shape == (149, 7), f"Expected (149, 7), got {df.shape}"


def test_no_missing_values():
    """Check that cleaned data has no missing values."""
    path = Path(__file__).parent.parent / "data" / "processed" / "cleaned_data.csv"
    df = pd.read_csv(path)
    assert df.isnull().sum().sum() == 0, "Cleaned data should have no missing values"


def test_no_duplicate_rows():
    """Check that cleaned data has no duplicate rows."""
    path = Path(__file__).parent.parent / "data" / "processed" / "cleaned_data.csv"
    df = pd.read_csv(path)
    assert df.duplicated().sum() == 0, "Cleaned data should have no duplicates"


def test_species_column_has_three_values():
    """Check that the species column has exactly 3 unique values."""
    path = Path(__file__).parent.parent / "data" / "processed" / "cleaned_data.csv"
    df = pd.read_csv(path)
    assert df['species'].nunique() == 3, "Should have exactly 3 species"


def test_data_loader_creates_directories():
    """Check that DataLoader creates raw and processed directories."""
    loader = DataLoader(data_dir="data")
    assert loader.raw_dir.exists(), "raw_dir should exist"
    assert loader.processed_dir.exists(), "processed_dir should exist"


def test_get_dataset_info_returns_expected_keys():
    """Check that get_dataset_info returns the expected dictionary keys."""
    loader = DataLoader(data_dir="data")
    df = pd.read_csv(loader.processed_dir / "cleaned_data.csv")
    info = loader.get_dataset_info(df)
    
    expected_keys = {'shape', 'column_info', 'memory_usage', 'sample'}
    assert expected_keys.issubset(info.keys()), "Missing expected keys in dataset info"


def test_derived_columns_exist():
    """Check that sepal_area and petal_area columns were correctly added."""
    path = Path(__file__).parent.parent / "data" / "processed" / "cleaned_data.csv"
    df = pd.read_csv(path)
    assert 'sepal_area' in df.columns, "sepal_area column should exist"
    assert 'petal_area' in df.columns, "petal_area column should exist"
