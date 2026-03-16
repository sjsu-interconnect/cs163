import joblib
import os
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier

def train():
    # Generate dummy data
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    
    # Train tree classifier
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X, y)
    
    # Ensure model directory exists
    os.makedirs('app/model', exist_ok=True)
    
    # Save the model
    joblib.dump(clf, 'app/model/tree_model.pkl')
    print("Model trained and saved to app/model/tree_model.pkl")

if __name__ == "__main__":
    train()
