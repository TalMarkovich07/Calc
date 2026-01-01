import calcFunctions as Fc
from calcFunctions import factorial
from calcExepctions import *


def find_after_dot(expression):
    """
    finds the fraction part of the number
    gets an expression that starts with digits
    returns the digits as a fraction and the length of the fraction
    """
    # returns the part of the number after the dot
    # also returns the length of the number after the dot
    num = 0
    for i in range(len(expression)):
        if not expression[i].isdigit():
            return num / 10 ** len(str(num)), i
        num *= 10
        num += int(expression[i])
    return num / 10 ** len(str(num)), len(expression)


def num_contains_semi(expression):
    """
    checks if the first number in the expression contains a semicolumn
    returns True or False
    """
    for char in expression:
        if char.isdigit():
            return False
        if char == '~':
            return True
    return False


def find_num(expression):
    """
    finds the first number in the expression
    :param expression:
    :return the first number in the expression and the first index after him:
    :raises exceptions if the number is wrong.
    """
    # gets an expression that's supposed to start with a number
    # returns the first number of the expression and the first index after him
    num = 0
    if expression == '':
        raise EmptyExpressionException()
    if not expression[0].isdigit():  # checks the cases where the expression doesn't start with a number
        if expression[0] == '~':
            if num_contains_semi(expression[1:]):  # if expression starts with '~', there must come a number after
                raise WrongInputAsOperandException("After ~ must come a number.")
            num, end = find_num(expression[1:])
            return -1 * num, end + 1
        elif expression[0] == '-':
            num, end = find_num(expression[1:])
            return -1 * num, end + 1
        elif expression[0] == '!':
            return Fc.factorial(find_num(expression[1:]))
        elif expression[0] == '(':
            end = handle_brackets(expression[1:])
            return run_calculator(expression[1:end]), end + 1
        else:
            raise WrongInputAsOperandException(f'{expression[0]} has no meaning to this calculator')
    i = 0
    while i < len(expression):
        if not expression[i].isdigit():
            if expression[i] == '.':
                after_dot, j = find_after_dot(expression[i + 1:])
                return num + after_dot, i + j + 1
            elif expression[i] == '!':
                return factorial(num), i + 1
            elif expression[i] == '#':
                return Fc.hashtag(num), i + 1
            return num, i
        num *= 10
        num += int(expression[i])
        i += 1
    return num, i


def op_level(op):
    """
    calculates the level of operation
    :param op: 
    :return: the level of operation
    :raises exception if the operation has no meaning
    """""
    match op:
        case '+':
            return 0
        case '-':
            return 0
        case '*':
            return 1
        case '/':
            return 1
        case '^':
            return 2
        case '%':
            return 3
        case '$':
            return 4
        case '&':
            return 4
        case '@':
            return 4
    raise WrongUseOfOperatorException(f'{op} has no meaning to this calculator')


def calculate_exp(a, op, b):
    """
    calculates given numbers and operator
    :param a: first number
    :param op: operator
    :param b: second number
    :return: the answer
    :raises exception if the operation has no meaning
    """
    match op:
        case '+':
            return Fc.add(a, b)
        case '-':
            return Fc.sub(a, b)
        case '*':
            return Fc.mul(a, b)
        case '/':
            return Fc.div(a, b)
        case '^':
            return Fc.pow(a, b)
        case '%':
            return Fc.mod(a, b)
        case '$':
            return Fc.max(a, b)
        case '&':
            return Fc.min(a, b)
        case '@':
            return Fc.avg(a, b)
    raise WrongUseOfOperatorException(f'{op} has no meaning to this calculator')

def pop_until(lst, level, x):
    """
    gets list of lists and calculates everything in the list and x
    :param lst: a list of lists containing previous expressions with higher level operators
    :param level: level of current operator
    :param x: number to do the last calculation on
    :return:
    """
    i = len(lst) - 1
    while i >= level:
        while len(lst[i]) > 0:
            op = lst[i].pop()
            y = lst[i].pop()
            print(f'current calculation: {y} {op} {x}')
            x = calculate_exp(y, op, x)
        i -= 1
    return x


def handle_brackets(expression):
    # gets an expression that starts with ( and returns the index of the last )
    """
    calculates the index of the last closing bracket
    :param expression: parameter that starts with ( and end with contains )
    :return: the index of the last closing bracket
    :raises exception if found more opening brackets than closing
    """
    cnt = 1
    for i in range(len(expression)):
        if expression[i] == '(':
            cnt += 1
        if expression[i] == ')':
            cnt -= 1
            if cnt == 0:
                return i + 1
    raise WrongUseOfOperatorException('Brackets were opened but were not closed')


def run_calculator(expression):
    """
    calculates the given expression
    :param expression: equation
    :return: the answer
    """
    expression = expression.replace(' ', '')
    expression = expression.strip()
    expression += '+0'
    lst = [[], [], [], [], []]
    # in this list we will keep all expressions that are of higher level
    x, end = find_num(expression)
    print(f'x={x}')
    operator = expression[end]
    print(f'operator={operator}')
    level = op_level(operator)
    print(f'level={level}')
    lst[level].append(x)
    lst[level].append(operator)
    expression = expression[end + 1:]
    # print(f'exp={exp}')
    while True:
        # in this loop, we want to find the next operator and calculate everything above his level
        x, end = find_num(expression)
        # print(f'x={x}')
        expression = expression[end:]
        if len(expression) <= 0:
            break
        operator = expression[0]
        # print(f'operator={operator}')
        if op_level(operator) > level:
            level = op_level(operator)
            lst[level].append(x)
            lst[level].append(operator)
        else:
            level = op_level(operator)
            x = pop_until(lst, level, x)
            lst[level].append(x)
            lst[level].append(operator)
        # print(f'lst={lst}')
        expression = expression[1:]
        # print(f'exp={exp}')
    # print(f'lst={lst}')
    return pop_until(lst, level, x)


if __name__ == '__main__':
    while True:
        exp = input('Enter expression, enter STOP to quit: ')
        if exp.lower() == 'stop':
            break
        try:
            calculated = run_calculator(exp)
            print(f'{exp} = {calculated}')
        except calcException as ce:
            print(ce)
