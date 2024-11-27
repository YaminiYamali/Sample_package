from .processing.preprocessing import preprocess_inputs
from .training_pipeline import load_model


def make_prediction(data):
    """
    Make a prediction for house prices given input features.
    
    Args:
    data (dict): A dictionary with keys 'area', 'bedrooms', 'age' representing
                 the house features.

    Returns:
    float: Predicted house price.
    """
    try:
        # Preprocess the input data
        processed_data = preprocess_inputs(data)
        
        # Load the trained model
        model = load_model()
        
        # Make predictions
        prediction = model.predict(processed_data)
        return prediction[0]
    
    except Exception as e:
        raise ValueError(f"An error occurred during prediction: {e}")
