# Funkcja określająca priorytety operatorów
def get_operator_weight(operator):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return operators.get(operator, 0)


def convert_to_rpn(expression):
    output = []
    operators_stack = []

    for element in expression.split():
        if element.isdigit():
            output.append(element)
        elif element == '(':
            operators_stack.append('(')
        elif element == ')':
            while operators_stack and operators_stack[-1] != '(':
                output.append(operators_stack.pop())
            operators_stack.pop()
        else:
            while operators_stack and get_operator_weight(operators_stack[-1]) >= get_operator_weight(element):
                output.append(operators_stack.pop())
            operators_stack.append(element)

    while operators_stack:
        output.append(operators_stack.pop())

    return ' '.join(output)


def convert_from_rpn(rpn_expression):
    stack = []

    for element in rpn_expression.split():
        if element.isdigit():
            stack.append(element)
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            stack.append(f'({num2}{element}{num1})')

    return stack[0]


expression = '2 + 3 * 4 - 5 + 7 * 6 / 3 - 2 * 3 ^ 2 + ( 5 - 2 ) * 2'
print(f'Expression: {expression}')
print(f'To RPN: {convert_to_rpn(expression)}')
print(f'From RPN: {convert_from_rpn(convert_to_rpn(expression))}')
