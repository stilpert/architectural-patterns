from interpreter import Multiplying, Addition, Context, Square, Subtraction, Variable
if __name__ == "__main__":
    ctx = Context()

    ctx.set_variable('x', 2)
    ctx.set_variable('y', 3)

    print('Addition', Addition(Variable('x'), Variable('y')).interpret(ctx))
    print('Subtraction', Subtraction(Variable('x'), Variable('y')).interpret(ctx))
    print('Multiplying', Multiplying(Variable('x'), Variable('y')).interpret(ctx))
    print('Square', Square(Variable('y')).interpret(ctx))
