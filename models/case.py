class Case:
    def __init__(self, x, y, definite_value=None):
        self.potential_values = list(range(1, 10))
        self.definite_value = None
        self.line = x
        self.column = y
        self.square = self.compute_square()

        if definite_value is not None:
            self.potential_values = [definite_value]
            self.definite_value = definite_value

    def eliminate(self, value):
        if type(value) == int:
            has_updated = self.eliminate_single_value(value)
        else:
            has_updated = self.eliminate_multiple_values(value)
        if len(self.potential_values) == 1:
            self.definite_value = self.potential_values[0]
        return has_updated

    def eliminate_single_value(self, value):
        if value in self.potential_values:
            self.potential_values.remove(value)
            return True
        return False

    def eliminate_multiple_values(self, values):
        if type(values) != list:
            raise Exception(f"Input: {values} should be a list of int")
        has_updated = False
        for value in values:
            has_updated |= self.eliminate_single_value(value)
        return has_updated

    def is_definitive(self):
        return self.definite_value is not None

    def set_definitive(self, value):
        if value not in self.potential_values:
            raise Exception(f"Value {value} is illegal for this case {self}")
        else:
            self.definite_value = value
            self.potential_values = [value]

    def potential_values_are_within(self, values):
        return len(set(self.potential_values) - set(values)) == 0

    # 123
    # 456
    # 789
    def compute_square(self):
        conversion = {
            0: [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
            1: [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]],
            2: [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]],
            3: [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]],
            4: [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]],
            5: [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]],
            6: [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]],
            7: [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]],
            8: [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]],
        }

        for square_number in conversion:
            if [self.line, self.column] in conversion[square_number]:
                return square_number

    def __str__(self):
        if self.definite_value is None:
            return " "
        else:
            return str(self.definite_value)

    def position(self):
        return f"({self.line}, {self.column})"
