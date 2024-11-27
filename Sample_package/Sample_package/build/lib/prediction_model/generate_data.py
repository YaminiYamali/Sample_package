import os

import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic data
def generate_data(num_samples):
    area = np.random.randint(500, 5000, size=num_samples)  # Area in square feet
    bedrooms = np.random.randint(1, 6, size=num_samples)   # Number of bedrooms
    age = np.random.randint(0, 30, size=num_samples)       # Age of the house
    # Price is a linear function of area, bedrooms, and age, plus some noise
    price = area * 150 + bedrooms * 50000 - age * 1000 + np.random.normal(0, 10000, size=num_samples)
    return pd.DataFrame({"area": area, "bedrooms": bedrooms, "age": age, "price": price})

# Generate train and test datasets
train_data = generate_data(1000)  # 1000 samples for training
test_data = generate_data(200)   # 200 samples for testing

# Save datasets to the `datasets` folder
datasets_path = os.path.join(os.path.dirname(__file__), 'datasets')
os.makedirs(datasets_path, exist_ok=True)

train_data_path = os.path.join(datasets_path, 'train.csv')
test_data_path = os.path.join(datasets_path, 'test.csv')

train_data.to_csv(train_data_path, index=False)
test_data.to_csv(test_data_path, index=False)

print(f"Train dataset saved to {train_data_path}")
print(f"Test dataset saved to {test_data_path}")
