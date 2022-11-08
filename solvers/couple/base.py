from solvers.mono import MonoSolver


class CoupleSolver(MonoSolver):
    couple_size = None

    @classmethod
    def solve_cases(cls, cases):
        has_updated = False
        unsolved_cases = cls.get_unsolved_cases(cases)
        for case in unsolved_cases:
            potential_couple = case.potential_values
            if len(potential_couple) != cls.couple_size:
                continue
            if cls.has_couple(cases, potential_couple):
                has_updated |= cls.update_known_couple(cases, potential_couple)
        return has_updated

    @staticmethod
    def get_unsolved_cases(cases):
        unsolved_cases = filter(lambda case: not case.is_definitive(), cases)
        return list(unsolved_cases)

    @classmethod
    def has_couple(cls, cases, couple_values):
        matches = 0
        for case in cases:
            if case.potential_values_are_within(couple_values):
                matches += 1
        return matches == cls.couple_size

    @staticmethod
    def update_known_couple(cases, couple_values):
        has_updated = False
        for case in cases:
            if not case.potential_values_are_within(couple_values):
                has_updated |= case.eliminate(couple_values)
        return has_updated
