import operator
import re

def calculate(expression: str) -> float:
    # Define supported operators and their corresponding functions
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    
    # Function to apply an operator to the top two numbers in the stack
    def apply_operator():
        if len(num_stack) < 2 or not op_stack:
            return
        b = num_stack.pop()
        a = num_stack.pop()
        op = op_stack.pop()
        num_stack.append(operators[op](a, b))
    
    # Helper function to process operator precedence and parentheses
    def process_operator(token):
        while op_stack and op_stack[-1] != '(' and operators.get(op_stack[-1]):
            apply_operator()
        op_stack.append(token)
    
    # Remove spaces from the expression
    expression = expression.replace("", "")
    
    # Regular expression to extract numbers, parentheses, and operators
    tokens = re.findall(r'\d+\.?\d*|[-+*/()]', expression)
    
    # Initialize number and operator stack
    num_stack = []
    op_stack = []
    
    # Process each token
    for token in tokens:
        if token in operators or token in '()':
            process_operator(token)
        else:
            # If token is a number, convert it to float and push to number stack
            num_stack.append(float(token))
    
    # Apply any remaining operators
    while op_stack:
        apply_operator

    # The result should be the only value left in the number stack
    return num_stack[0] if num_stack else 0.0
