class Person:
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.age}yo'

    def __eq__(self, other):
        if self.age == other:
            return True
        return False

    def __add__(self, num: int):
        self.age += num
        return self.age

    def myMethod(self):
        print('tratata')

    # def __add__(self, obj:float):
    #     return self.age + obj.age


p1 = Person('Иван', "Иванов", 13)
p2 = Person("Петро", "Петров", 19)

# print(p1 + p2)
# print(p1 + 6)
# print(p1.age)
# print(p1 == p2)

li = [p1, p2]

for i in li:
    if i == 13:
        print(i)


class MyPerson(Person):
    def __eq__(self, other: Person):
        if self.firstname == other.firstname and \
                self.lastname == other.lastname and \
                self.age == other.age:
            return True
        return False
    def myMethod(self):
        print('trutututu')

mp1 = MyPerson('vasa', 'pupkin', 13)
mp2 = MyPerson('vasa', 'pupkin', 13)
print(mp1)
if mp1 == mp2:
    print('ooo')
else:
    print('aaa')
mp1.myMethod()