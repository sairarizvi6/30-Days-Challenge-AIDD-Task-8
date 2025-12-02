import streamlit as st
import sys
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator.main import Calculator
from src.utils.errors import CalculatorError

st.set_page_config(layout="wide")

st.title("Advanced Calculator")

# Initialize calculator in session state
if 'calculator' not in st.session_state:
    st.session_state.calculator = Calculator()

calculator = st.session_state.calculator

# Input for the mathematical expression
expression = st.text_input("Enter a mathematical expression:", "", key="expression_input")

# Button to trigger calculation
calculate_button = st.button("Calculate")

# Clear History button
if st.button("Clear History"):
    calculator.clear_history()
    st.rerun()

# Display area for results and history
result_placeholder = st.empty()

if calculate_button and expression:
    try:
        result = calculator.calculate(expression)
        result_placeholder.success(f"Result: {result}")
    except CalculatorError as e:
        result_placeholder.error(f"Calculation Error: {e}")
    except Exception as e:
        result_placeholder.error(f"An unexpected error occurred: {e}")
else:
    result_placeholder.info("Enter an expression and click Calculate.")

st.subheader("Calculation History")
history_entries = calculator.get_history()

if history_entries:
    # Display history in reverse chronological order
    for entry in reversed(history_entries):
        st.write(f"{entry["timestamp"]}: {entry["expression"]} = {calculator.formatter.format_result(entry["result"])}")
else:
    st.write("No calculations in history yet.")
