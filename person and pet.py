class Dog:
    def __init__(self, dog_name: str, dage: int, tricks: list = []):
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

    def train_dog(self, new_trick):
        print(f"I try to teach {self.name} {new_trick},\n"
              f"{self.name}: 'you old dog always have new tricks'")
        self.tricks.append(new_trick)

class Person:
    def __init__(self, pname: str, person_age: int, pet: Dog):
        self.name = pname
        self.age = person_age
        self.dog = pet

    def walk_dog(self):
        print("The dog looks at me, says no")


dog = Dog(dog_name="Rabbit", dage=4)
person_one = Person(pname="R.H", person_age=25, pet=dog)
person_one.dog.sit()
#person_one.dog.bark()
new_tricks = input("Please enter the trick you want to teach: ")
person_one.dog.train_dog(new_trick=new_tricks)
print(f"I want to walk my dog")
person_one.walk_dog()
print(person_one.dog.tricks)
