"""
Perceptron - Basic Neural Network Building Block
"""

import random


class Perceptron:
    """
    A single-layer perceptron for binary classification.
    Implements the basic building block of neural networks.
    """
    
    def __init__(self, num_inputs, learning_rate=0.1):
        """
        Initialize perceptron with random weights.
        
        Args:
            num_inputs: Number of input features
            learning_rate: Learning rate for weight updates
        """
        self.learning_rate = learning_rate
        self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
        self.bias = random.uniform(-1, 1)
    
    def activation(self, x):
        """
        Step activation function.
        
        Args:
            x: Input value
            
        Returns:
            1 if x >= 0, else 0
        """
        return 1 if x >= 0 else 0
    
    def predict(self, inputs):
        """
        Make a prediction for given inputs.
        
        Args:
            inputs: Feature vector
            
        Returns:
            Predicted class (0 or 1)
        """
        # Calculate weighted sum
        total = sum(w * x for w, x in zip(self.weights, inputs))
        total += self.bias
        
        # Apply activation function
        return self.activation(total)
    
    def train(self, training_data, epochs=100):
        """
        Train the perceptron using the perceptron learning rule.
        
        Args:
            training_data: List of (inputs, label) tuples
            epochs: Number of training epochs
        """
        for epoch in range(epochs):
            errors = 0
            
            for inputs, label in training_data:
                prediction = self.predict(inputs)
                error = label - prediction
                
                if error != 0:
                    errors += 1
                    # Update weights: w = w + learning_rate * error * input
                    for i in range(len(self.weights)):
                        self.weights[i] += self.learning_rate * error * inputs[i]
                    self.bias += self.learning_rate * error
            
            # Early stopping if no errors
            if errors == 0:
                print(f"Converged at epoch {epoch + 1}")
                break
    
    def evaluate(self, test_data):
        """
        Evaluate accuracy on test data.
        
        Args:
            test_data: List of (inputs, label) tuples
            
        Returns:
            Accuracy (0 to 1)
        """
        correct = 0
        for inputs, label in test_data:
            if self.predict(inputs) == label:
                correct += 1
        return correct / len(test_data)
