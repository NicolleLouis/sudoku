from service.solver_service import SolverService


class BaseSolver:
    iterate = list(range(9))

    def __init__(self, grid):
        self.grid = grid
        self.service = SolverService(grid)

    def run(self):
        has_updated = self.step()
        while has_updated:
            has_updated = self.step()

    def step(self):
        raise NotImplementedError('step')
