from models.case import Case


class BaseGenerator:
    def __init__(self, raw_values):
        self.raw_values = raw_values

    def generate(self):
        raise NotImplementedError("generate")

    @staticmethod
    def generate_case_from_raw_value(raw_value, x, y):
        if raw_value in [" ", "0"]:
            return Case(x=x, y=y)
        else:
            return Case(x=x, y=y, definite_value=int(raw_value))
