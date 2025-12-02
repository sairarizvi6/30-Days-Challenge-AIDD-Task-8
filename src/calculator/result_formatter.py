class ResultFormatter:
    def __init__(self, precision: int = 10):
        self.precision = precision

    def format_result(self, result: float) -> str:
        # Convert to string and strip trailing zeros for cleaner integer representation
        if result == int(result):
            return str(int(result))

        # Format floating-point numbers with specified precision
        # Use f-string for controlled precision and general formatting
        formatted_result = f"%0.{self.precision}f" % result

        # Remove trailing zeros after decimal point, if any
        formatted_result = formatted_result.rstrip('0')
        # If the number ends with a decimal point (e.g., "5."), remove it
        if formatted_result.endswith('.'):
            formatted_result = formatted_result.rstrip('.')

        return formatted_result
