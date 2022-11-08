class GridVisualisation:
    def __init__(self, grid):
        self.grid = grid

    def display_grid(self):
        for line in self.grid.values:
            display_line = ""
            for case in line:
                display_line += str(case)
            print(display_line)

    def display_grid_state(self):
        print("#########")
        if self.grid.is_solved():
            print("Grid is solved congrats")
        else:
            print("Grid is not solved")
            print(f"{81 - self.grid.number_of_definitive_values()} cases to guess")
        self.display_grid()

    def detail_coordinate(self, x, y):
        case = self.grid.values[x][y]
        if case.is_definitive():
            print(f"Definitive value: {case.definite_value}")
        else:
            print(f"Potential values: {case.potential_values}")

    def missing_data(self):
        for line in self.grid.values:
            for case in line:
                if not case.is_definitive():
                    print(f"{case.position()}: {len(case.potential_values)} "
                          f"potentials -> {case.potential_values}")
