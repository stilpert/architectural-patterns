class Operation:
    def __init__(self, left_expression, right_expression):
        self.left_expression = left_expression
        self.right_expression = right_expression

    def interpret():
        return None

    def get_operands(self, context):
        return self.left_expression.interpret(context), self.right_expression.interpret(context)


class Addition(Operation):

    def interpret(self, context):
        l, r = self.get_operands(context)
        return l + r


class Subtraction(Operation):

    def interpret(self, context):
        l, r = self.get_operands(context)
        return l - r


class Multiplying(Operation):
    def interpret(self, context):
        l, r = self.get_operands(context)
        return l * r


class Square(Operation):
    def __init__(self, left_expression):
        self.left_expression = left_expression
        self.right_expression = left_expression

    def interpret(self, context):
        l, r = self.get_operands(context)
        return l * r


class Variable():
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        return context.get_variable(self.name)


class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        return self.variables.get(name)
