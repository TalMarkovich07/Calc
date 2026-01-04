import calcExepctions as Ce
from calcExepctions import WrongFactorialException


def add(a:float, b:float):
    return a+b
def sub(a:float, b:float):
    return a-b
def mul(a:float ,b:float):
    return a*b
def div(a:float, b:float):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b
def pow(a:float, b:float):
    if b * len(str(a)) >= 4300:
        raise Ce.NumberTooLargeException()
    return a**b
def mod(a:float ,b:float):
    return a%b
def max(a:float, b:float):
    if a > b:
        return a
    else:
        return b
def min(a:float, b:float):
    if a < b:
        return a
    else:
        return b
def avg(a:float, b:float):
    return (a+b)/2
def neg(a:float):
    return a*-1
def factorial(n:int):
    if n < 0:
        raise WrongFactorialException(f'Cannot factorial {n} number because he is negative')
    if n > 997:
        raise Ce.NumberTooLargeException()
    elif float(int(n)) != n:
        raise Ce.FactorialOfFloatException()
    elif n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
def hashtag(n:float):
    if n < 0:
        raise Ce.HastagDoneOnNegativeException()
    string_num = str(n)
    sum = 0
    for ch in string_num:
        if ch.isdigit():
            sum += int(ch)
    return sum