import pandas as pd
from pathlib import Path
import os


def load_data(file_path: str | Path) -> pd.DataFrame:
    '''
    Loads CSV data into pandas DataFrame.

    Args:
      file_path (str | Path): Path to the CSV file.

    Returns:
      pd.DataFrame: Loaded dataset.
    '''

    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return pd.read_csv(file_path)
