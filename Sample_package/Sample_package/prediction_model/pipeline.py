import os

import pandas as pd

from .predict import make_prediction
from .processing.data_handling import load_dataset
from .processing.data_handling import save_data
from .processing.data_handling import summarize_dataset
from .training_pipeline import load_model
from .training_pipeline import train_model


def run_pipeline():
    # Paths to datasets
    train_file = os.path.join(os.path.dirname(__file__), 'datasets/train.csv')
    test_file = os.path.join(os.path.dirname(__file__), 'datasets/test.csv')

    # Step 1: Load and summarize the datasets
    print("\n=== Step 1: Load and Summarize Datasets ===")
    train_data = load_dataset(train_file)
    test_data = load_dataset(test_file)
    print("Training Data:")
    summarize_dataset(train_data)
    print("\nTesting Data:")
    summarize_dataset(test_data)

    # Step 2: Train the model
    print("\n=== Step 2: Train the Model ===")
    train_model()

    # Step 3: Test the model
    print("\n=== Step 3: Test the Model ===")
    model = load_model()

    # Extract features from the test set
    X_test = test_data[['area', 'bedrooms', 'age']]
    y_test = test_data['price']

    # Make predictions on the test set
    predictions = model.predict(X_test)
    test_data['predicted_price'] = predictions

    # Save predictions to a file
    predictions_file = os.path.join(os.path.dirname(__file__), 'datasets/test_predictions.csv')
    save_data(test_data, predictions_file)

    # Evaluate the model's performance
    print("\n=== Step 4: Evaluate Model Performance ===")
    mse = ((y_test - predictions) ** 2).mean()
    print(f"Mean Squared Error on Test Set: {mse:.2f}")

    # Step 5: Make a single prediction
    print("\n=== Step 5: Make a Single Prediction ===")
    sample_input = {"area": 2000, "bedrooms": 3, "age": 10}
    prediction = make_prediction(sample_input)
    print(f"Prediction for input {sample_input}: ${prediction:.2f}")

if __name__ == "__main__":
    run_pipeline()
