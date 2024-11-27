import os
import pickle

from sklearn.linear_model import LinearRegression

from .processing.data_handling import load_dataset


def train_model():
    """
    Train the house price prediction model using the train dataset.
    """
    # Use load_dataset to load the training data
    file_path = os.path.join(os.path.dirname(__file__), 'datasets/train.csv')
    data = load_dataset(file_path)

    # Features and target
    X = data[['area', 'bedrooms', 'age']]
    y = data['price']

    # Train the model
    model = LinearRegression()
    model.fit(X, y)

    # Save the trained model
    model_path = os.path.join(os.path.dirname(__file__), 'trained_models/house_price_model.pkl')
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    print("Model trained and saved at", model_path)

def load_model():
    """
    Load the trained house price prediction model from the saved file.
    """
    # Path to the trained model
    model_path = os.path.join(os.path.dirname(__file__), 'trained_models/house_price_model.pkl')

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"The model file does not exist at {model_path}")

    with open(model_path, 'rb') as f:
        return pickle.load(f)
