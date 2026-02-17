"""
Linear Regression Algorithm
"""


class LinearRegression:
    """
    Simple linear regression using gradient descent.
    Fits a line y = mx + b to data.
    """
    
    def __init__(self, learning_rate=0.0001, iterations=1000):
        """
        Initialize linear regression model.
        
        Args:
            learning_rate: Step size for gradient descent
            iterations: Number of training iterations
        
        Note: Learning rate is tuned for typical house price scale data.
        For data on different scales, consider feature scaling or adjusting this value.
        """
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.m = 0.0  # slope
        self.b = 0.0  # intercept
    
    def fit(self, X, y):
        """
        Train the model using gradient descent.
        
        Args:
            X: Training features (list of numbers)
            y: Training labels (list of numbers)
        """
        n = len(X)
        
        for _ in range(self.iterations):
            # Make predictions
            y_pred = [self.m * x + self.b for x in X]
            
            # Calculate gradients
            dm = (-2/n) * sum((y[i] - y_pred[i]) * X[i] for i in range(n))
            db = (-2/n) * sum(y[i] - y_pred[i] for i in range(n))
            
            # Update parameters
            self.m -= self.learning_rate * dm
            self.b -= self.learning_rate * db
    
    def predict(self, X):
        """
        Make predictions for new data.
        
        Args:
            X: Feature values (list of numbers or single number)
            
        Returns:
            Predicted values
        """
        if isinstance(X, list):
            return [self.m * x + self.b for x in X]
        else:
            return self.m * X + self.b
    
    def score(self, X, y):
        """
        Calculate R-squared score.
        
        Args:
            X: Test features
            y: True values
            
        Returns:
            R-squared score (0 to 1, higher is better)
        """
        y_pred = self.predict(X)
        
        # Calculate total sum of squares
        y_mean = sum(y) / len(y)
        ss_tot = sum((yi - y_mean) ** 2 for yi in y)
        
        # Calculate residual sum of squares
        ss_res = sum((y[i] - y_pred[i]) ** 2 for i in range(len(y)))
        
        # R-squared
        return 1 - (ss_res / ss_tot)
