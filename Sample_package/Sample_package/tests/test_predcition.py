import unittest

import pandas as pd

from ..prediction_model.predict import make_prediction


class TestPrediction(unittest.TestCase):
    def test_make_prediction(self):
        test_data = {"area": 1200, "bedrooms": 3, "age": 10}
        prediction = make_prediction(test_data)
        self.assertGreater(prediction, 0)  # Prediction should be positive

    def test_bulk_predictions(self):
        # Load test dataset
        test_file_path = 'Sample_package/prediction_model/datasets/test.csv'
        test_data = pd.read_csv(test_file_path)
        
        # Make predictions for the first 5 rows
        for i, row in test_data.head(5).iterrows():
            input_data = {"area": row["area"], "bedrooms": row["bedrooms"], "age": row["age"]}
            prediction = make_prediction(input_data)
            self.assertGreater(prediction, 0)  # Prediction should be positive

    def test_invalid_data(self):
        invalid_data = {"area": None, "bedrooms": 3, "age": 10}
        with self.assertRaises(ValueError):
            make_prediction(invalid_data)

if __name__ == '__main__':
    unittest.main()
