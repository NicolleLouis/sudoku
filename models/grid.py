from solvers.direct_elimination import DirectEliminationSolver
from solvers.couple.double import DoubleSolver
from solvers.fill_hole import FillHoleSolver
from solvers.couple.quadruple import QuadrupleSolver
from solvers.couple.triple import TripleSolver
from solvers.pointer import PointerSolver
from visualisation.grid import GridVisualisation


class Grid:
    def __init__(self, values):
        self.values = values
        self.visualisation = GridVisualisation(self)
        self.solvers = [
            DirectEliminationSolver(self),
            FillHoleSolver(self),
            DoubleSolver(self),
            TripleSolver(self),
            QuadrupleSolver(self),
            PointerSolver(self),
        ]

    def number_of_definitive_values(self):
        number_of_definitive_values = 0
        for line in self.values:
            for case in line:
                if case.is_definitive():
                    number_of_definitive_values += 1
        return number_of_definitive_values

    def number_of_potential_values(self):
        number_of_potential_values = 0
        for line in self.values:
            for case in line:
                number_of_potential_values += len(case.potential_values)
        return number_of_potential_values

    def is_solved(self):
        return self.number_of_definitive_values() == 81

    def solve(self, display=True):
        should_continue = True
        while should_continue:
            initial_potential_numbers = self.number_of_potential_values()
            self.step()
            if display:
                self.visualisation.display_grid_state()
            final_potential_numbers = self.number_of_potential_values()
            if self.is_solved():
                should_continue = False
            if initial_potential_numbers == final_potential_numbers:
                should_continue = False

    def step(self):
        for solver in self.solvers:
            solver.run()

    def get_line(self, x):
        return self.values[x]

    def get_column(self, y):
        return list(
            map(
                lambda line: line[y], self.values
            )
        )

    def get_square(self, n):
        square_cases = []
        for line in self.values:
            for case in line:
                if case.square == n:
                    square_cases.append(case)
        return square_cases
