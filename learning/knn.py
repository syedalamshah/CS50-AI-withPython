"""
K-Nearest Neighbors Classification Algorithm
"""

import math
from collections import Counter


class KNearestNeighbors:
    """
    K-Nearest Neighbors classifier.
    Classifies data points based on majority vote of k nearest neighbors.
    """
    
    def __init__(self, k=3):
        """
        Initialize KNN classifier.
        
        Args:
            k: Number of neighbors to consider
        """
        self.k = k
        self.X_train = None
        self.y_train = None
    
    def fit(self, X, y):
        """
        Train the model (just store the training data).
        
        Args:
            X: Training features (list of lists)
            y: Training labels (list)
        """
        self.X_train = X
        self.y_train = y
    
    def euclidean_distance(self, point1, point2):
        """
        Calculate Euclidean distance between two points.
        
        Args:
            point1: First point (list of features)
            point2: Second point (list of features)
            
        Returns:
            Euclidean distance as float
        """
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
    
    def predict_one(self, x):
        """
        Predict class for a single data point.
        
        Args:
            x: Feature vector to classify
            
        Returns:
            Predicted class label
        """
        # Calculate distances to all training points
        distances = []
        for i, x_train in enumerate(self.X_train):
            dist = self.euclidean_distance(x, x_train)
            distances.append((dist, self.y_train[i]))
        
        # Sort by distance and get k nearest
        distances.sort(key=lambda x: x[0])
        k_nearest = distances[:self.k]
        
        # Get labels of k nearest neighbors
        k_labels = [label for _, label in k_nearest]
        
        # Return most common label
        return Counter(k_labels).most_common(1)[0][0]
    
    def predict(self, X):
        """
        Predict classes for multiple data points.
        
        Args:
            X: Feature vectors to classify (list of lists)
            
        Returns:
            List of predicted class labels
        """
        return [self.predict_one(x) for x in X]
    
    def score(self, X, y):
        """
        Calculate accuracy on test set.
        
        Args:
            X: Test features
            y: True labels
            
        Returns:
            Accuracy (0 to 1)
        """
        predictions = self.predict(X)
        correct = sum(pred == true for pred, true in zip(predictions, y))
        return correct / len(y)
