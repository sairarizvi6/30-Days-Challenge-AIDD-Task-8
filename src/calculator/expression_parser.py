import re
from typing import List
from src.utils.errors import InvalidExpressionError, log_error

class ExpressionParser:
    def __init__(self):
        self.operators = {
            '+': {'precedence': 2, 'associativity': 'left'},
            '-': {'precedence': 2, 'associativity': 'left'},
            '*': {'precedence': 3, 'associativity': 'left'},
            '/': {'precedence': 3, 'associativity': 'left'},
            '%': {'precedence': 3, 'associativity': 'left'},
            '^': {'precedence': 4, 'associativity': 'right'},
        }

    def tokenize(self, expression: str) -> List[str]:
        # Use regex to split the expression into numbers, operators, and parentheses
        # This regex handles decimal numbers and keeps parentheses and operators as separate tokens
        tokens = re.findall(r'\d+\.?\d*|\.\d+|[+\-*/%^()]|', expression)
        tokens = [token for token in tokens if token.strip()]

        # Handle unary minus/plus (e.g., -5, -(2+3))
        processed_tokens = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '-' or token == '+':
                # Check if it's a unary operator
                if i == 0 or (processed_tokens and processed_tokens[-1] in self.operators and processed_tokens[-1] != ')'):
                    # If it's a unary minus/plus, append it to the next number or (expression)
                    if i + 1 < len(tokens) and re.match(r'\d+\.?\d*|\.\d+', tokens[i+1]):
                        processed_tokens.append(token + tokens[i+1])
                        i += 1
                    elif i + 1 < len(tokens) and tokens[i+1] == '(':
                        # Unary operator before parenthesis, e.g. -(2+3). Treat as -1 * (2+3)
                        processed_tokens.append(token + '1')
                        processed_tokens.append('*')
                        processed_tokens.append('(')
                        i += 1
                    else:
                        processed_tokens.append(token)
                else:
                    processed_tokens.append(token)
            else:
                processed_tokens.append(token)
            i += 1

        return processed_tokens

    def shunting_yard(self, expression: str) -> List[str]:
        tokens = self.tokenize(expression)
        output_queue = []
        operator_stack = []

        for token in tokens:
            if re.match(r'^\d+\.?\d*|\.\d+|[+\-]?\d+\.?\d*$', token):  # If token is a number (including unary numbers)
                output_queue.append(token)
            elif token in self.operators:  # If token is an operator
                while operator_stack and operator_stack[-1] != '(' and \
                      (self.operators[operator_stack[-1]]['precedence'] > self.operators[token]['precedence'] or \
                       (self.operators[operator_stack[-1]]['precedence'] == self.operators[token]['precedence'] and \
                        self.operators[token]['associativity'] == 'left')):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack or operator_stack[-1] != '(':
                    log_error(f"Mismatched parentheses in expression: {expression}")
                    raise InvalidExpressionError("Mismatched parentheses", expression=expression)
                operator_stack.pop()  # Pop the '('

        while operator_stack:
            if operator_stack[-1] == '(' or operator_stack[-1] == ')':
                log_error(f"Mismatched parentheses in expression: {expression}")
                raise InvalidExpressionError("Mismatched parentheses", expression=expression)
            output_queue.append(operator_stack.pop())

        return output_queue
