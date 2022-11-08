from solvers.base import BaseSolver


class PointerSolver(BaseSolver):
    def step(self):
        has_updated = False
        for n in self.iterate:
            square_cases = self.grid.get_square(n)
            has_updated |= self.solve_square(square_cases, n)
        return has_updated

    def solve_square(self, square_cases, square_number):
        has_updated = False
        missing_numbers = self.service.missing_numbers(square_cases)
        for number in missing_numbers:
            potential_cases = self.service.matching_cases(cases=square_cases, number=number)
            has_updated |= self.analyse_column(
                value=number,
                potential_cases=potential_cases,
                square_number=square_number,
            )
            has_updated |= self.analyse_line(
                value=number,
                potential_cases=potential_cases,
                square_number=square_number,
            )
        return has_updated

    @classmethod
    def get_columns(cls, cases):
        return set(map(lambda case: case.column, cases))

    @classmethod
    def get_lines(cls, cases):
        return set(map(lambda case: case.line, cases))

    def analyse_column(self, value, potential_cases, square_number):
        potential_columns = self.get_columns(potential_cases)
        if len(potential_columns) == 1:
            return self.remove_from_column_outside_square(
                value=value,
                square_number=square_number,
                column_number=list(potential_columns)[0]
            )
        return False

    def remove_from_column_outside_square(self, value, square_number, column_number):
        has_updated = False
        column_cases = self.grid.get_column(column_number)
        for case in column_cases:
            if case.square == square_number:
                continue
            if case.is_definitive():
                continue
            has_updated |= case.eliminate(value=value)
        return has_updated

    def analyse_line(self, value, potential_cases, square_number):
        potential_lines = self.get_lines(potential_cases)
        if len(potential_lines) == 1:
            return self.remove_from_line_outside_square(
                value=value,
                square_number=square_number,
                line_number=list(potential_lines)[0]
            )
        return False

    def remove_from_line_outside_square(self, value, square_number, line_number):
        has_updated = False
        line_cases = self.grid.get_line(line_number)
        for case in line_cases:
            if case.square == square_number:
                continue
            if case.is_definitive():
                continue
            has_updated |= case.eliminate(value=value)
        return has_updated
