class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        return {'name': self.name, 'surname': self.surname, 'age': self.age}

    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}'


class Student(Person):
    spec = 'Agrarnoe delo'

    def isSuccesful(self, mean_score):
        return True if mean_score > 75 else False


p1 = Person('Vasa', 'Pupkin', 33)
print(p1)

s1 = Student('Petya', 'Kopitov', 21)
print(s1.isSuccesful(56))
