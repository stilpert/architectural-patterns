import unittest
from interpreter import Context, Variable, Addition, Multiplying, Subtraction, Square

ctx = Context()

ctx.set_variable('x', 2)
ctx.set_variable('y', 3)


class TestAddition(unittest.TestCase):

    def test_addition(self):
        res = Addition(Variable('x'), Variable('y')).interpret(ctx)
        self.assertEqual(res, 5)


class TestSubtraction(unittest.TestCase):

    def test_subtraction(self):
        res = Subtraction(Variable('x'), Variable('y')).interpret(ctx)
        self.assertEqual(res, -1)


class TestMultiplying(unittest.TestCase):

    def test_multiplying(self):
        res = Multiplying(Variable('x'), Variable('y')).interpret(ctx)
        self.assertEqual(res, 6)


class TestSquare(unittest.TestCase):

    def test_square(self):
        res = Square(Variable('y')).interpret(ctx)
        self.assertEqual(res, 9)


class TestContext(unittest.TestCase):

    def test_set_val(self):
        ctx = Context()

        ctx.set_variable('x', 2)
        self.assertEqual(Variable('x').interpret(ctx), 2)

        ctx.set_variable('x', 3)
        self.assertEqual(Variable('x').interpret(ctx), 3)


if __name__ == "__main__":
    unittest.main()
