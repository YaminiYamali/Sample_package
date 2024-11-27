# config.py - Configuration file for the prediction model pipeline

import os

# Base directory for the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path for datasets
DATASET_DIR = os.path.join(BASE_DIR, 'prediction_model/datasets')
TRAIN_DATA_PATH = os.path.join(DATASET_DIR, 'train.csv')
TEST_DATA_PATH = os.path.join(DATASET_DIR, 'test.csv')

# Path for trained models
MODEL_DIR = os.path.join(BASE_DIR, 'prediction_model/trained_models')
MODEL_PATH = os.path.join(MODEL_DIR, 'house_price_model.pkl')

# Logging configuration
LOGGING_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE_PATH = os.path.join(LOGGING_DIR, 'model_training.log')

# Add any other configurations, e.g., model hyperparameters, etc.
MODEL_HYPERPARAMETERS = {
    'alpha': 0.01,
    'max_iter': 1000,
}

# Set the logging level (optional)
LOGGING_LEVEL = 'INFO'

# You can also add other configurations based on the needs of your project
