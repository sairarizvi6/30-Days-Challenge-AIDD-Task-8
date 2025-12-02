import re
from src.utils.errors import InvalidExpressionError, log_error

class InputSanitizer:
    def __init__(self):
        # Allowed characters: digits, operators (+, -, *, /, ^, %), parentheses, decimal point
        self.allowed_pattern = re.compile(r"^[0-9+\-*/%^().\s]*$")

    def sanitize(self, expression: str) -> str:
        if not isinstance(expression, str):
            log_error(f"Input must be a string, got {type(expression)}")
            raise TypeError("Input expression must be a string")

        # Remove all whitespace for consistent processing
        sanitized_expression = expression.replace(" ", "")

        # Check for disallowed characters
        if not self.allowed_pattern.match(sanitized_expression):
            log_error(f"Expression contains disallowed characters: {expression}")
            raise InvalidExpressionError("Expression contains disallowed characters", expression=expression)

        return sanitized_expression
