from generator.base_generator import BaseGenerator
from models.grid import Grid


# Closest to the truth
# Input looks like real data: Array of Array
class GridGenerator(BaseGenerator):
    def generate(self):
        values = []
        x = 0
        for raw_line in self.raw_values:
            line = []
            y = 0
            for raw_value in raw_line:
                case = self.generate_case_from_raw_value(raw_value, x, y)
                line.append(case)
                y += 1
            values.append(line)
            x += 1
        return Grid(values)
