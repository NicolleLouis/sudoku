from solvers.mono import MonoSolver


class FillHoleSolver(MonoSolver):
    needed_numbers = list(range(1, 10))

    def solve_cases(self, cases):
        has_updated = False
        missing_numbers = self.service.missing_numbers(cases)
        for missing_number in missing_numbers:
            if self.number_of_options(cases, missing_number) == 1:
                self.fill_hole(cases, missing_number)
                has_updated = True
        return has_updated

    @classmethod
    def fill_hole(cls, cases, number):
        for case in cases:
            if not case.is_definitive():
                if number in case.potential_values:
                    case.set_definitive(number)

    @classmethod
    def number_of_options(cls, cases, number):
        number_of_options = 0
        for case in cases:
            if not case.is_definitive():
                if number in case.potential_values:
                    number_of_options += 1
        return number_of_options
