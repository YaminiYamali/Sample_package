import pandas as pd


def validate_inputs(data):
    """
    Validates the input data to ensure all required fields are present and valid.

    Args:
    data (dict): Input data containing house features.

    Raises:
    ValueError: If input data contains missing or invalid values.
    """
    required_columns = ['area', 'bedrooms', 'age']
    
    # Check for missing columns
    for column in required_columns:
        if column not in data:
            raise ValueError(f"Missing required field: '{column}'")
    
    # Check for missing or None values
    if any(data[column] is None for column in required_columns):
        raise ValueError("Input data contains missing values!")
    
    # Check for negative or invalid values
    if data['area'] <= 0 or data['bedrooms'] <= 0 or data['age'] < 0:
        raise ValueError("Input data contains invalid (negative or zero) values!")

def preprocess_inputs(data):
    """
    Preprocesses the input data to prepare it for model prediction.

    Args:
    data (dict): Input data containing house features.

    Returns:
    pd.DataFrame: Preprocessed data as a DataFrame, ready for prediction.
    """
    # Validate the input data
    validate_inputs(data)
    
    # Convert input dictionary to a DataFrame
    input_df = pd.DataFrame([data])
    
    # Ensure the order of columns matches the training dataset
    required_columns = ['area', 'bedrooms', 'age']
    return input_df[required_columns]
