import calcExepctions as Ce
from calcExepctions import WrongFactorialException


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b
def pow(a,b):
    if b * len(str(a)) >= 4300:
        raise Ce.NumberTooLargeException()
    return a**b
def mod(a,b):
    return a%b
def max(a,b):
    if a > b:
        return a
    else:
        return b
def min(a,b):
    if a < b:
        return a
    else:
        return b
def avg(a,b):
    return (a+b)/2
def neg(a):
    return a*-1
def factorial(n):
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
def hashtag(n):
    if n < 0:
        raise Ce.HastagDoneOnNegativeException()
    string_num = str(n)
    sum = 0
    for ch in string_num:
        if ch.isdigit():
            sum += int(ch)
    return sum