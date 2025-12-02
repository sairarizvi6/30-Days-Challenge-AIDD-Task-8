import re
from src.utils.errors import InvalidExpressionError, log_error

class ExpressionValidator:
    def __init__(self):
        # Regex to check for valid number formats (integers, decimals)
        self.number_pattern = re.compile(r"\d+(\.\d*)?|\.\d+")
        # Regex to check for valid operators
        self.operator_pattern = re.compile(r"[+\-*/%^]")

    def validate(self, expression: str) -> bool:
        if not isinstance(expression, str):
            log_error(f"Input must be a string, got {type(expression)}")
            raise TypeError("Input expression must be a string")

        if not expression:
            log_error("Expression is empty.")
            raise InvalidExpressionError("Expression cannot be empty")

        # Check for balanced parentheses
        if not self._check_balanced_parentheses(expression):
            log_error(f"Unbalanced parentheses in expression: {expression}")
            raise InvalidExpressionError("Unbalanced parentheses", expression=expression)

        # Check for invalid characters (already done by sanitizer, but good to have a backup)
        if not re.fullmatch(r"[0-9+\-*/%^().]*", expression):
            log_error(f"Expression contains invalid characters: {expression}")
            raise InvalidExpressionError("Expression contains invalid characters", expression=expression)

        # Check for operators with no operands, or multiple operators in a row
        if re.search(r"[+\-*/%^]{2,}", expression) or \
           re.search(r"[+\-*/%^][)}\s]*[+\-*/%^]", expression): # e.g., 1++2, (2*)3
            log_error(f"Invalid operator placement: {expression}")
            raise InvalidExpressionError("Invalid operator placement", expression=expression)

        # Check for operators at the beginning or end (unless it's a unary minus/plus)
        if re.match(r"[*/%^]", expression) or re.search(r"[+\-*/%^]$", expression):
            log_error(f"Operator at invalid position: {expression}")
            raise InvalidExpressionError("Operator at invalid position", expression=expression)

        # Check for invalid decimal points (e.g., 1..2, .)
        if re.search(r"\.{2,}", expression) or re.search(r"(^|[^\d])\.(?!\d)|\.(?!\d)($|[^\d])", expression):
             log_error(f"Invalid decimal point usage: {expression}")
             raise InvalidExpressionError("Invalid decimal point usage", expression=expression)

        return True

    def _check_balanced_parentheses(self, expression: str) -> bool:
        balance = 0
        for char in expression:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False  # Closing parenthesis without open one
        return balance == 0
