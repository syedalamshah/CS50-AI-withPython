"""
Example: Machine Learning algorithms
KNN Classification and Linear Regression
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from learning import KNearestNeighbors, LinearRegression


def knn_example():
    """
    Example of K-Nearest Neighbors classification.
    Iris flower classification with simple 2D features.
    """
    print("=== K-Nearest Neighbors Example ===\n")
    
    # Simple iris dataset (sepal length, sepal width) -> species
    # 0 = setosa, 1 = versicolor
    X_train = [
        [5.1, 3.5], [4.9, 3.0], [4.7, 3.2], [4.6, 3.1],  # setosa
        [7.0, 3.2], [6.4, 3.2], [6.9, 3.1], [5.5, 2.3],  # versicolor
    ]
    y_train = [0, 0, 0, 0, 1, 1, 1, 1]
    
    # Test data
    X_test = [
        [5.0, 3.6],  # should be setosa
        [6.7, 3.0],  # should be versicolor
    ]
    y_test = [0, 1]
    
    # Train and predict
    knn = KNearestNeighbors(k=3)
    knn.fit(X_train, y_train)
    
    predictions = knn.predict(X_test)
    accuracy = knn.score(X_test, y_test)
    
    print("Training samples:", len(X_train))
    print(f"Test predictions: {predictions}")
    print(f"Accuracy: {accuracy * 100:.1f}%")
    
    for i, (x, pred, true) in enumerate(zip(X_test, predictions, y_test)):
        species = "setosa" if pred == 0 else "versicolor"
        correct = "✓" if pred == true else "✗"
        print(f"  Sample {i+1}: {x} -> {species} {correct}")


def linear_regression_example():
    """
    Example of Linear Regression.
    Predict house prices based on square footage.
    """
    print("\n\n=== Linear Regression Example ===\n")
    
    # Simple dataset: square footage -> price (in $1000s)
    X_train = [600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
    y_train = [150, 180, 220, 250, 280, 320, 350, 380]
    
    # Test data
    X_test = [900, 1500]
    y_test = [200, 300]
    
    # Train model
    model = LinearRegression(learning_rate=0.0001, iterations=1000)
    model.fit(X_train, y_train)
    
    # Make predictions
    predictions = model.predict(X_test)
    r_squared = model.score(X_test, y_test)
    
    print("Training samples:", len(X_train))
    print(f"Model: Price = {model.m:.4f} * sqft + {model.b:.2f}")
    print(f"R² score: {r_squared:.4f}\n")
    
    print("Predictions:")
    for sqft, pred, true in zip(X_test, predictions, y_test):
        print(f"  {sqft} sqft -> ${pred:.1f}K (actual: ${true}K)")


def main():
    """Run machine learning examples"""
    knn_example()
    linear_regression_example()


if __name__ == "__main__":
    main()
