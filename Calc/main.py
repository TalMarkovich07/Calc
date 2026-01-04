from calcFunctions import *
from calcExepctions import *

def semi_in_num(expression):
    """
    counts how many semicolons appear in the expression
    :param expression:
    :return cnt: number of semicolons
    """
    cnt = 0
    for char in expression:
        if char == '~':
            cnt+=1
    return cnt

def find_num(expression):
    """
    finds the first number in the expression
    :param expression:
    :return num, index: first number in the expression and the first index after him
    :raises exception: if the number doesn't follow omega's calculator rules
    """
    number_string = '' # a string for the current number
    unary_minus = False # tells us if there is a unary minus
    another_minus = True # says if there can be another minus or not (will become false after 1 digit)

    if expression == '':
        raise EmptyExpressionException()

    if not (expression[0].isdigit() or expression[0] == '-' or expression[0] == '~'):  # checks the cases where the expression doesn't start with a number
        if expression[0] == '(':
            end = handle_brackets(expression[1:])
            return run_calculator(expression[1:end]), end + 1
        else:
            raise WrongInputAsOperandException(f'Operand cannot start with {expression[0]}')
    i = 0
    while i < len(expression): #main loop - checks digits, dots and unary operators
        if not (expression[i].isdigit() or expression[i] == '.' or expression[i] == '!' or expression[i] == '#'):
            if expression[i] == '-':
                unary_minus = True
            elif unary_minus and expression[i] != '(':
                raise WrongInputAsOperandException(f'After unary minus must come a number')
            if not another_minus:
                if expression[i] == '~':
                    raise WrongUseOfOperatorException('~ cannot appear in the end of a number')
                else:
                    return calculate_num(expression[:i]), i
            else:
                if expression[i] == '~' or expression[i] == '-':
                    number_string += expression[i]
                else:
                    return calculate_num(expression[:i]), i

        else:
            another_minus = False
            unary_minus = False
            number_string += expression[i]
        i+=1
    return calculate_num(number_string), i


def calculate_num(num_string: str):
    """
    calculates the number inside the expression
    :param num_string:
    :return num: the number that was calculated
    :raises WrongUseOfOperatorException: if number has more than 1 ~
    :raises WrongInputException: if the expression ends with something that don't make sense
    """
    another_digit = True
    if num_string == '-':
        return -1
    if semi_in_num(num_string) > 1:
        raise WrongUseOfOperatorException('Semicolon must be before a number and not an expression.')
    minus = 1
    is_deci = False
    deci = 0
    num = 0
    for i in range(len(num_string)):
        if num_string[i] == '-': #check is positive or negative
            minus = -1* minus
        elif num_string[i] == '.':
            is_deci = True
        elif num_string[i].isdigit():
            if not another_digit:
                raise WrongInputAsOperandException(f'Operand cannot contain {num_string[i-1]} in the middle')
            if is_deci:
                deci+=int(num_string[i])
                deci*=10
            else:
                num+=int(num_string[i])
                if i<len(num_string)-1 and num_string[i+1].isdigit():
                    num*=10
        else:
            if num_string[i] == '!':
                if is_deci:
                    raise WrongFactorialException('Cannot factorial decimals')
                num = factorial(num)
                another_digit = False
            elif num_string[i] == '#':
                num = hashtag(num)
                if is_deci:
                    num += hashtag(deci)
                    is_deci = False
                another_digit = False
    if is_deci:
        deci = float(deci) / 10**(len(str(deci)))
        num = float(num) + deci

    if semi_in_num(num_string) == 1:
        num = -1*num

    return num * minus



def op_level(op):
    """
    calculates the level of operator
    :param op: operator
    :return: the level of the given operator
    :raises exception if the operator has no meaning
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
    raise WrongUseOfOperatorException(f'{op} cannot be used as an operator')


def calculate_exp(a:int, op:str, b:int):
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
            return add(a, b)
        case '-':
            return sub(a, b)
        case '*':
            return mul(a, b)
        case '/':
            return div(a, b)
        case '^':
            return pow(a, b)
        case '%':
            return mod(a, b)
        case '$':
            return max(a, b)
        case '&':
            return min(a, b)
        case '@':
            return avg(a, b)
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
            x = calculate_exp(y, op, x)
        i -= 1
    return x


def handle_brackets(expression):
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
    if expression[0] == '-':
        expression = '0' + expression
    if expression == '':
        raise EmptyExpressionException()
    expression += '+0'
    lst = [[], [], [], [], []] # in this list we will keep all expressions that are of higher level
    x, end = find_num(expression)
    operator = expression[end]
    level = op_level(operator)
    lst[level].append(x)
    lst[level].append(operator)
    expression = expression[end + 1:]
    while True: # in this loop, we want to find the next operator and calculate everything above his level
        x, end = find_num(expression)
        expression = expression[end:]
        if len(expression) <= 0:
            break
        operator = expression[0]
        if op_level(operator) > level:
            level = op_level(operator)
            lst[level].append(x)
            lst[level].append(operator)
        else:
            level = op_level(operator)
            x = pop_until(lst, level, x)
            lst[level].append(x)
            lst[level].append(operator)
        expression = expression[1:]
    return pop_until(lst, level, x)


if __name__ == '__main__':
    while True:
        exp = input('Enter expression, enter STOP to quit: ')
        if exp.lower() == 'stop':
            break
        try:
            calculated = run_calculator(exp)
            if calculated == float(int(calculated)):
                calculated = int(calculated)
            print(f'{exp} = {calculated}')
        except calcException as ce:
            print(f'My exception occurred: {ce}')
        except Exception as ex:
            print(f'Program exception occurred: {ex}')

