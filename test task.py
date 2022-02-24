class Car:
    """
    data items: make(str), model(str), year(int)
    behaviour to_string()
    """

    def __init__(self, car_make, car_model, car_year):
        self.make = car_make
        self.model = car_model
        self.year = car_year

    def drive(self):
        print(f"Driving my {self.year} {self.make} {self.model} #{self.to_string()}")

    def to_string(self):
        return f"Car {self.make} {self.model} {self.year}"


my_car = Car(car_make="Chevrolet", car_model="idk", car_year=2016)
print(my_car.make)
# 两种方式结果一样，第一种更好，引用更直接
my_car.drive()
Car.drive(my_car)

print(my_car.to_string())
