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


# d1 = Dog("jessi", "girl", 3)
# print(d1.name, d1.gender)
# d2 = Dog("hoski", "boy", 13)
# print(d2.name, d2.gender)

# d1.eat()
# d2.eat()

# d1.bark(False)
# d2.bark(True)

class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")
class Teacher(Person):
           
    def teach(self):
        print(f'master {self.name} is teaching')

teacher1 = Teacher("sara", "blalalal", 35)
teacher1.teach()
teacher1.eat()

class Student(Person):
    def __init__(self, name, family, age, grade):
        super().__init__( name, family, age)
        self.grade = grade

    def exam(self):
        if self.grade in ('A', 'B'):
            print(f"{self.name}'s exam was so good.")
        else:
            print(f"{self.name}'s exam was  not so good.")


student1 = Student("armin", "amini", 18, 'A')
student2 = Student("arman", "amani", 17, 'B')
student3 = Student("aryan", "amyni", 19, 'C')

student1.exam()
student2.exam()
student3.exam()
student1.eat()
