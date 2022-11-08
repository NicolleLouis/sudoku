from solvers.base import BaseSolver


class MonoSolver(BaseSolver):
    def step(self):
        has_updated = self.update_info_lines()
        has_updated |= self.update_info_columns()
        has_updated |= self.update_info_squares()
        return has_updated

    def update_info_lines(self):
        return self.update_info(self.grid.get_line)

    def update_info_columns(self):
        return self.update_info(self.grid.get_column)

    def update_info_squares(self):
        return self.update_info(self.grid.get_square)

    def update_info(self, callback):
        has_updated = False
        for n in self.iterate:
            cases = callback(n)
            has_updated |= self.solve_cases(cases)
        return has_updated

    @classmethod
    def solve_cases(cls, cases) -> bool:
        raise NotImplementedError("solve_cases")
