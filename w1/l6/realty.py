class Realty:
    def __init__(self, name: str, area: float):
        if area is None:
            raise ValueError("Area can't be None")
        self.name = name
        self.area = area

    def greet(self):
        return f"Hello, {self.name}"

    @staticmethod
    def calculate_monthly_payment(value: int, years: int, interest_rate: float) -> float:
        monthly_interest = interest_rate / 12
        overall_interest = (1.0 + monthly_interest) ** (years * 12)
        monthly_payment = value * monthly_interest * overall_interest / (overall_interest - 1.0)

        return monthly_payment

    @classmethod
    def load_from_file(cls, filepath: str):
        with open(filepath) as fin:
            name, area = fin.read().strip().split()
            area = float(area)
            return cls(name=name, area=area)

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}), area={self.area}"

    def __eq__(self, other):
        """
        Function compares two objects of class Realty by parameters (name and area)

        :param other:
        :return: Equality of objects
        """
        outcome = (
            (self.name == other.name)
            and (self.area == other.area)
        )
        return outcome
