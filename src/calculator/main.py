from src.calculator.input_sanitizer import InputSanitizer
from src.calculator.expression_validator import ExpressionValidator
from src.calculator.expression_parser import ExpressionParser
from src.calculator.expression_evaluator import ExpressionEvaluator
from src.calculator.result_formatter import ResultFormatter
from src.history.calculator_history import CalculatorHistory
from src.utils.errors import CalculatorError, log_error

class Calculator:
    def __init__(self):
        self.sanitizer = InputSanitizer()
        self.validator = ExpressionValidator()
        self.parser = ExpressionParser()
        self.evaluator = ExpressionEvaluator()
        self.formatter = ResultFormatter()
        self.history = CalculatorHistory()

    def calculate(self, expression: str) -> str:
        try:
            # 1. Sanitize input
            sanitized_expression = self.sanitizer.sanitize(expression)
            log_error(f"Sanitized expression: {sanitized_expression}", level=20) # INFO

            # 2. Validate expression
            self.validator.validate(sanitized_expression)
            log_error(f"Validated expression: {sanitized_expression}", level=20) # INFO

            # 3. Parse operators and operands (to postfix)
            postfix_expression = self.parser.shunting_yard(sanitized_expression)
            log_error(f"Postfix expression: {postfix_expression}", level=20) # INFO

            # 4. Evaluate postfix expression
            result = self.evaluator.evaluate_postfix(postfix_expression)
            log_error(f"Evaluated result: {result}", level=20) # INFO

            # 5. Store in history
            self.history.add_entry(expression, result)

            # 6. Format and return result
            formatted_result = self.formatter.format_result(result)
            log_error(f"Formatted result: {formatted_result}", level=20) # INFO
            return formatted_result
        except CalculatorError as e:
            log_error(f"Calculator error: {e}")
            return f"Error: {e}"
        except Exception as e:
            log_error(f"An unexpected error occurred: {e}")
            return f"Error: An unexpected error occurred: {e}"

    def get_history(self):
        return self.history.get_history()

    def clear_history(self):
        self.history.clear_history()
