from calcExepctions import FactorialOfFloatException


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
        raise ValueError('Cannot factorial negative numbers')
    elif float(int(n)) != n:
        raise FactorialOfFloatException()
    elif n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)