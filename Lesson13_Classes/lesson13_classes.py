class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

dog1 = Dog('Max', 3)
dog2 = Dog('Moon', 5)

print(dog1.name)
print(dog2.name)

class Car:

    def __init__(self, Brand, Model, Year):

        self.name = Brand
        self.model = Model
        self.year = Year

        pass

car1 = Car('Nissan', 'Sentra', 2026)
car2 = Car('Buick', 'LeSabre', 1997)

print(car1.name, car1.model, car1.year)
print(car2.name, car2.model, car2.year)

class student:

    def __init__(self, name):

        self.name = name

        pass

    def introduce(self):
        print('Hi! My name is ', self.name)

Student = student('Trystan')

Student.introduce()