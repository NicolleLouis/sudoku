from generator.base_generator import BaseGenerator
from models.grid import Grid


# Take data from https://sudoku.com/ website (Thanks :) )
# Input is an array of all data, 0 is empty value
class SudokuComGenerator(BaseGenerator):
    def generate(self):
        values = []
        for index in range(len(self.raw_values)):
            raw_value = self.raw_values[index]
            x = index//9
            y = index % 9
            case = self.generate_case_from_raw_value(raw_value, x, y)
            if y == 0:
                values.append([case])
            else:
                values[x].append(case)
        return Grid(values)
