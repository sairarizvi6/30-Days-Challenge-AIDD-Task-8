import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CalculatorError(Exception):
    """Custom exception for calculator-related errors."""
    pass

class InvalidExpressionError(CalculatorError):
    """Exception raised for invalid mathematical expressions."""
    def __init__(self, message="Invalid mathematical expression", expression=None):
        super().__init__(message)
        self.expression = expression

class DivisionByZeroError(CalculatorError):
    """Exception raised for division by zero errors."""
    def __init__(self, message="Division by zero is not allowed", expression=None):
        super().__init__(message)
        self.expression = expression


def log_error(message, level=logging.ERROR):
    logging.log(level, message)
