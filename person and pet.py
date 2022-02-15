class Dog:
    def __init__(self, dog_name: str, dage: int, tricks: []):
        self.name = dog_name
        self.age = dage
        self.tricks = tricks

    def bark(self):
        pass

    def sit(self):
        pass


class Person:
    def __init__(self, pname: str, person_age: int, pet: Dog):
        self.name = pname
        self.age = person_age
        self.dog = pet

    def walk_dog(self):
        pass

    def train_dog(self):
        pass


dog = Dog(dog_name="Akira", dage=4, tricks="hunting bird")
person_one = Person(pname="R.H", person_age=25, pet=dog)
print(person_one.dog.name)
