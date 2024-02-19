class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


# my_dog = Dog('Willie', 6)
# print(my_dog.name)
# print(my_dog.age)

# my_dog.sit()

# my_dog.roll_over()

class Car:
    """汽车"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def validate_rebuild(self, arg1, arg2):
        print(f"super {arg1} {arg2}")


class ElecticCar(Car):
    """电动汽车"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def validate_rebuild(self, arg1, arg2, arg3):
        print(f"child {arg1} {arg2} {arg3}")


my_car = ElecticCar('tesla', 'model s', 2019)
print(my_car.get_descriptive_name())

my_car.validate_rebuild('arg1', 'arg2', 'arg3')
