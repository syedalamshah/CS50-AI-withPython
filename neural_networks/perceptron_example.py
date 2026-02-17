"""
Example: Perceptron learning
Logic gates (AND, OR) using perceptron
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from neural_networks import Perceptron


def train_and_gate():
    """Train perceptron to learn AND logic gate"""
    print("=== Training Perceptron for AND Gate ===\n")
    
    # AND gate truth table
    training_data = [
        ([0, 0], 0),
        ([0, 1], 0),
        ([1, 0], 0),
        ([1, 1], 1),
    ]
    
    # Create and train perceptron
    perceptron = Perceptron(num_inputs=2, learning_rate=0.1)
    perceptron.train(training_data, epochs=100)
    
    # Test
    print("AND Gate Results:")
    for inputs, expected in training_data:
        prediction = perceptron.predict(inputs)
        correct = "✓" if prediction == expected else "✗"
        print(f"  {inputs[0]} AND {inputs[1]} = {prediction} (expected {expected}) {correct}")
    
    accuracy = perceptron.evaluate(training_data)
    print(f"\nAccuracy: {accuracy * 100:.1f}%")


def train_or_gate():
    """Train perceptron to learn OR logic gate"""
    print("\n\n=== Training Perceptron for OR Gate ===\n")
    
    # OR gate truth table
    training_data = [
        ([0, 0], 0),
        ([0, 1], 1),
        ([1, 0], 1),
        ([1, 1], 1),
    ]
    
    # Create and train perceptron
    perceptron = Perceptron(num_inputs=2, learning_rate=0.1)
    perceptron.train(training_data, epochs=100)
    
    # Test
    print("OR Gate Results:")
    for inputs, expected in training_data:
        prediction = perceptron.predict(inputs)
        correct = "✓" if prediction == expected else "✗"
        print(f"  {inputs[0]} OR {inputs[1]} = {prediction} (expected {expected}) {correct}")
    
    accuracy = perceptron.evaluate(training_data)
    print(f"\nAccuracy: {accuracy * 100:.1f}%")


def main():
    """Run perceptron examples"""
    train_and_gate()
    train_or_gate()
    
    print("\n\nNote: Perceptron cannot learn XOR gate (not linearly separable)")
    print("XOR requires multi-layer neural network")


if __name__ == "__main__":
    main()
