from solvers.mono import MonoSolver


class DirectEliminationSolver(MonoSolver):
    @classmethod
    def solve_cases(cls, cases):
        has_updated = False
        for case in cases:
            if case.is_definitive():
                case_has_updated = cls.eliminate_values(cases, case.definite_value)
                has_updated |= case_has_updated
        return has_updated

    @staticmethod
    def eliminate_values(cases, value):
        has_updated = False
        for case in cases:
            if not case.is_definitive():
                case_has_updated = case.eliminate(value)
                has_updated |= case_has_updated
        return has_updated
