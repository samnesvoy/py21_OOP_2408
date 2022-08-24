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
    def __init__(self, name, surname, age, spec):
        self.spec = spec
        super().__init__(name, surname, age)

    def isSuccesful(self, mean_score):
        return True if mean_score > 75 else False

    def __str__(self):
        return f'{super().__str__()}\nSpec: {self.spec}'


p1 = Person('Vasa', 'Pupkin', 33)
print(p1)

s1 = Student('Petya', 'Kopitov', 21)
print(s1)
