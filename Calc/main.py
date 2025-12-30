from unittest import case

import calcFunctions as fc
from calcExepctions import calcException, WrongInputAsOperandException, WrongUseOfOperatorException
from calcFunctions import factorial
from calcExepctions import *


def find_num(exp):
# gets an expression
# returns the first number of the expression and the fisrt index after him
    num = 0
    if exp == '':
        raise EmptyExpressionException()
    if not exp[0].isdigit():
        if exp[0]=='~':
            if exp[1]=='~':
                raise WrongInputAsOperandException("Two ~ were entered. that's not allowed!")
            return -1*find_num(exp[1:])
        elif exp[0]=='-':
            return -1*find_num(exp[1:])
        elif exp[0]=='!':
            return fc.factorial(find_num(exp[1:]))
        elif exp[0]=='(':
            end = handle_brackets(exp[1:])
            return run_calculator(exp[1:end-1]), end+1
        else:
            raise WrongInputAsOperandException(f'{exp[0]} has no meaning to this calculator')
    i = 0
    while i<len(exp):
        if not exp[i].isdigit():
            #if exp[i]=='.':
            #    after_dot, j = find_after_dot(exp[i+1:])
            #    return num+after_dot, i+j+1
            if exp[i] == '!':
                return factorial(num), i+1
            return num, i
        num*=10
        num+=int(exp[i])
        i+=1
    return num, i

def op_level(op):
# gets an operand and return it's level
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
def calculate_exp(a, op, b):
#gets operand 1, operator and operand2, and caculates it
    match op:
        case '+':
            return fc.add(a,b)
        case '-':
            return fc.sub(a,b)
        case '*':
            return fc.mul(a,b)
        case '/':
            return fc.div(a,b)
        case '^':
            return fc.pow(a,b)
        case '%':
            return fc.mod(a,b)
        case '$':
            return fc.max(a,b)
        case '&':
            return fc.min(a,b)
        case '@':
            return fc.avg(a,b)

def pop_until(lst, level, x):
    #collect and solves everthing in the higher and equal level
    i = len(lst)-1
    while i>=level:
        while len(lst[i])>0:
            op = lst[i].pop()
            y = lst[i].pop()
            print(f'current calculation: {y} {op} {x}')
            x = calculate_exp(y, op, x)
        i-=1
    return x

def handle_brackets(exp):
    #gets an expression that starts with ( and returns the index of the last )
    cnt = 1
    for i in range(len(exp)):
        if exp[i]=='(':
            cnt += 1
        if exp[i]==')':
            cnt -= 1
            if cnt == 0:
                return i+1
    raise WrongUseOfOperatorException('Brakets were opened but were not closed')

def run_calculator(exp):
    exp = exp.replace(' ', '')
    exp = exp.strip()
    exp+='+0'
    lst = [[], [], [], [], []]
    #in this list we will keep all of the expressions that are of higher level
    x, end = find_num(exp)
    #print(f'x={x}')
    operator = exp[end]
    #print(f'operator={operator}')
    level = op_level(operator)
    #print(f'level={level}')
    lst[level].append(x)
    lst[level].append(operator)
    exp = exp[end+1:]
    #print(f'exp={exp}')
    y = 0
    while True:
        #in this loop, we want to find the next operator and calulate everything above his level
        x, end = find_num(exp)
        #print(f'x={x}')
        exp = exp[end:]
        if(len(exp)<=0):
            break
        operator = exp[0]
        #print(f'operator={operator}')
        if(op_level(operator)>level):
            level = op_level(operator)
            lst[level].append(x)
            lst[level].append(operator)
        else:
            level = op_level(operator)
            x = pop_until(lst, level, x)
            lst[level].append(x)
            lst[level].append(operator)
        #print(f'lst={lst}')
        exp = exp[1:]
        #print(f'exp={exp}')
    #print(f'lst={lst}')
    return pop_until(lst, level, x)



if __name__ == '__main__':
    while True:
        exp = input('Enter expression, enter STOP to quit: ')
        if exp.lower()=='stop':
            break
        try:
            calculated = run_calculator(exp)
            print(f'{exp} = {calculated}')
        except calcException as ce:
            print(ce)
