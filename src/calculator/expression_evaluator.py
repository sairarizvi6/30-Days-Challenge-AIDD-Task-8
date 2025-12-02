from typing import List
from src.utils.errors import DivisionByZeroError, InvalidExpressionError, log_error
import math

class ExpressionEvaluator:
    def __init__(self):
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': self._divide,
            '%': lambda x, y: x % y,
            '^': lambda x, y: x ** y,
        }

    def _divide(self, x, y):
        if y == 0:
            log_error("Attempted division by zero.")
            raise DivisionByZeroError("Division by zero is not allowed")
        return x / y

    def evaluate_postfix(self, postfix_expression: List[str]) -> float:
        operand_stack = []

        for token in postfix_expression:
            if token in self.operators:  # If token is an operator
                if len(operand_stack) < 2:
                    log_error(f"Insufficient operands for operator {token} in postfix expression: {postfix_expression}")
                    raise InvalidExpressionError("Insufficient operands for operator", expression=' '.join(postfix_expression))
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = self.operators[token](operand1, operand2)
                operand_stack.append(result)
            else:  # If token is an operand
                try:
                    operand_stack.append(float(token))
                except ValueError:
                    log_error(f"Invalid number format encountered: {token} in postfix expression: {postfix_expression}")
                    raise InvalidExpressionError(f"Invalid number format: {token}", expression=' '.join(postfix_expression))

        if len(operand_stack) != 1:
            log_error(f"Invalid expression - final stack size: {len(operand_stack)} for postfix expression: {postfix_expression}")
            raise InvalidExpressionError("Invalid expression format", expression=' '.join(postfix_expression))

        return operand_stack[0]
