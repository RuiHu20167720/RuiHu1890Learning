from dataclasses import dataclass


@dataclass
class Car:
    make: str
    model: str
    year: int

    def drive(self):
        print(f"Driving my {self.year} {self.make} {self.model} ")

    def to_string(self):
        return f"Car {self.make} {self.model} {self.year}"


my_car = Car(make="Chevrolet", model="idk", year=2016)
print(my_car.make)
my_car.drive()
print(my_car.to_string())
