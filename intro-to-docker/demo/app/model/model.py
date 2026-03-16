import joblib
import os

# Get the directory of the current file to build an absolute path to the model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'tree_model.pkl')

# Load the model globally so it's ready for inference
try:
    clf = joblib.load(model_path)
except FileNotFoundError:
    clf = None

def predict(features: list):
    """Predict the class given a list of features."""
    if clf is None:
        raise RuntimeError("Model not loaded. Please run train.py first.")
    
    # sklearn expects a 2D array, so we wrap features in a list
    prediction = clf.predict([features])
    return int(prediction[0])