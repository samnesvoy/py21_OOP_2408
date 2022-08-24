class Person:

    def __init__(self, name, surname, age):
        self.__name = ''
        self.__surname = ''
        self.__age = 0

        self.set_name(name)
        self.set_surname(surname)
        self.set_age(age)

    def set_name(self, name: str):
        self.__name = name.capitalize()

    def get_name(self):
        return self.__name

    def set_surname(self, surname: str):
        self.__surname = surname.capitalize()

    def get_surname(self):
        return self.__surname

    def set_age(self, age):
        if str(age).isdigit() and int(age) > 0:
            self.__age = age

    def get_age(self):
        return self.__age

    def get_info(self):
        return {'name': self.__name, 'surname': self.__surname, 'age': self.__age}

    def __str__(self):
        return f'Name: {self.__name}\nSurname: {self.__surname}\nAge: {self.__age}'


class Student(Person):
    def __init__(self, name, surname, age, spec):
        self.__spec = spec
        super().__init__(name, surname, age)

    def isSuccesful(self, mean_score):
        return True if mean_score > 75 else False

    def __str__(self):
        return f'{super().__str__()}\nSpec: {self.__spec}'


p1 = Person('vAsA', 'Pupkin', 33)
print(p1)

s1 = Student('Petya', 'Kopitov', 21, 'Аграрное дело')
print(s1)
