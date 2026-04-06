import cmath
import math

class DiscriminantStrategy:
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b * b - 4 * a * c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = b * b - 4 * a * c
        return d if d >= 0 else float('nan')


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        d = self.strategy.calculate_discriminant(a, b, c)

        if math.isnan(d):
            return (complex(float('nan'), float('nan')),
                    complex(float('nan'), float('nan')))

        sqrt_d = cmath.sqrt(d)
        return (
            (-b + sqrt_d) / (2 * a),
            (-b - sqrt_d) / (2 * a)
        )



solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
print(solver.solve(1, 10, 16))