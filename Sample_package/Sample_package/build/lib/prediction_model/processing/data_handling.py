import os

import pandas as pd


def load_dataset(file_path):
    """
    Loads a dataset from a CSV file.

    Args:
    file_path (str): The path to the dataset file.

    Returns:
    pd.DataFrame: The loaded dataset.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    return pd.read_csv(file_path)

def save_data(data, file_path):
    """
    Saves a DataFrame to a CSV file.

    Args:
    data (pd.DataFrame): The data to save.
    file_path (str): The path where the data will be saved.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    data.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

def summarize_dataset(data):
    """
    Prints a summary of the dataset.

    Args:
    data (pd.DataFrame): The dataset to summarize.
    """
    print("Dataset Summary:")
    print(data.info())
    print("\nMissing Values:")
    print(data.isnull().sum())
    print("\nDescriptive Statistics:")
    print(data.describe())
