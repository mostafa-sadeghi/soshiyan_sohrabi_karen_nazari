class Dog:
    def __init__(self, dog_name, dog_gender, dog_age):
        self.name = dog_name
        self.gender = dog_gender
        self.age = dog_age

    def eat(self):
        if self.gender == "boy":
            print(f"{self.name}, Good boy Eat Up")
        else:
            print(f"{self.name}, Good girl Eat Up")

    def bark(self, is_loud):
        if is_loud:
            print("WOOF WOOF WOOF")
        else:
            print("WOOF")


d1 = Dog("jessi", "girl", 3)
print(d1.name, d1.gender)
d2 = Dog("hoski", "boy", 13)
print(d2.name, d2.gender)

d1.eat()
d2.eat()

d1.bark(False)
d2.bark(True)
