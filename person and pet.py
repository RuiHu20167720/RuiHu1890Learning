class Dog:
    def __init__(self, dog_name: str, dage: int, tricks: []):
        self.name = dog_name
        self.age = dage
        self.tricks = tricks

    def bark(self):
        print("Woof, Woof")

    def sit(self):
        print("░░░░░░░░░░▄▄▄▄▄▄\n"
              "░░░░░░░░▄▀█▀█▄██████████▄▄\n"
              "░░░░░░░▐██████████████████▌\n"
              "░░░░░░░███████████████████▌\n"
              "░░░░░░▐███████████████████▌\n"
              "░░░░░░█████████████████████▄\n"
              "░░░▄█▐█▄█▀█████████████▀█▄█▐█▄\n"
              "░▄██▌██████▄█▄█▄█▄█▄█▄█████▌██▌\n"
              "████▄▀▀▀▀████████████▀▀▀▀▄███\n"
              "▐█████████▄▄▄▄▄▄▄▄▄▄▄▄██████▀\n"
              "░░░▀▀████████████████████▀\n"
              "░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐\n"
              "░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌\n"
              "░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌\n"
              "▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐\n"
              "▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌\n"
              "▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐\n"
              "░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌\n"
              "░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐\n"
              "░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌")


class Person:
    def __init__(self, pname: str, person_age: int, pet: Dog):
        self.name = pname
        self.age = person_age
        self.dog = pet

    def walk_dog(self):
        print("The dog looks at me, says no")

    def train_dog(self):
        print("I try to teach the dog some tricks,\n"
              "Dog: 'you old dog always have new tricks'")


dog = Dog(dog_name="Akira", dage=4, tricks="hunting bird")
person_one = Person(pname="R.H", person_age=25, pet=dog)
person_one.dog.sit()
person_one.dog.bark()
person_one.train_dog()
person_one.walk_dog()
