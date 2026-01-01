class calcException(Exception):
    def __init__(self, message):
        super(calcException, self).__init__(message)
class WrongUseOfOperatorException(calcException):
    def __init__(self, message):
        super(WrongUseOfOperatorException, self).__init__(message)

class WrongInputAsOperandException(calcException):
    def __init__(self, message):
        super(WrongInputAsOperandException, self).__init__(message)

class FactorialOfFloatException(calcException):
    def __init__(self):
        super(FactorialOfFloatException, self).__init__('Cannot factorial numbers that are not whole numbers')

class EmptyExpressionException(calcException):
    def __init__(self):
        super(EmptyExpressionException, self).__init__('Expression is empty')

class NumberTooLargeException(calcException):
    def __init__(self):
        super(NumberTooLargeException, self).__init__('Number is too large. Please type smaller numbers.')