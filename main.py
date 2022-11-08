from generator.sudoku_com import SudokuComGenerator

raw_data = "070530106002000007000080000050008000004650030000002600000006000900000040020170300"

generator = SudokuComGenerator(raw_values=raw_data)

grid = generator.generate()
grid.visualisation.display_grid_state()
grid.solve(display=True)
if not grid.is_solved():
    print("Missing Data:")
    grid.visualisation.missing_data()
