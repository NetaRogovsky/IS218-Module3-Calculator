class Addition:
    @staticmethod
    def execute(a, b):
        return a + b


class Subtraction:
    @staticmethod
    def execute(a, b):
        return a - b


class Multiplication:
    @staticmethod
    def execute(a, b):
        return a * b


class Division:
    @staticmethod
    def execute(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b