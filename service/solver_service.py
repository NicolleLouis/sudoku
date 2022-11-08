class SolverService:
    needed_numbers = list(range(1, 10))

    def __init__(self, grid):
        self.grid = grid

    @classmethod
    def filled_numbers(cls, cases):
        filled_numbers = []
        for case in cases:
            if case.is_definitive():
                filled_numbers.append(case.definite_value)
        return filled_numbers

    @classmethod
    def missing_numbers(cls, cases):
        return list(set(cls.needed_numbers) - set(cls.filled_numbers(cases)))

    @staticmethod
    def matching_cases(cases, number):
        matching_cases = []
        for case in cases:
            if number in case.potential_values:
                matching_cases.append(case)
        return matching_cases
