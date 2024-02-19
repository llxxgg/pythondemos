from car import Car


class ElecticCar(Car):
    """电动汽车"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def validate_rebuild(self, arg1, arg2, arg3):
        print(f"child {arg1} {arg2} {arg3}")
