import time


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
        self.__name = '75'

    def isSuccesful(self, mean_score):
        return True if mean_score > 75 else False

    def __str__(self):
        self.__name
        self.get_name()
        return f'{super().__str__()}\nSpec: {self.__spec}'


# p1 = Person('vAsA', 'Pupkin', 33)
# print(p1)
#
# s1 = Student('Petya', 'Kopitov', 21, 'Аграрное дело')
# print(s1)

# pricesUSD = [100, 35, 67.99, 25.5]
# print(pricesUSD)
USDrate = 39.5


# декорирующая функция
def changePriceDecorator_v1(myFunction):
    # print("Hello! Let's change your prices...")

    def simpleWrapper(argList):
        print("I've got list of prices with {} elements.Function starts working...".format(len(argList)))
        result = myFunction(argList)
        resultwithDisc = list(map(lambda x: x * (1 - 0.15), result))
        print("Let's set a discount..")
        return resultwithDisc

    return simpleWrapper


# декорируем функцию
@changePriceDecorator_v1
def toPriceNew(priceList):
    return list(map(lambda x: x * USDrate, priceList))


# print(toPriceNew(pricesUSD))
# Создаем новую функцию с помощью декоратора и целевой функции
# pricesToVIPClients = changePriceDecorator_v1(toPriceNew)

# print(pricesToGRN(pricesUSD))

# класс декоратор
class Decorator:
    def __init__(self, fn):
        # декорируемая функция
        self.fn = fn

    def __call__(self, num1, num2):
        # при вызове будет выполнятся декорируемая функция плюс что-то еще
        return self.fn(num1, num2) ** 2


# @Decorator
def add_nums(num1, num2):
    return num1 + num2


@Decorator
def add_nums1(num1, num2):
    return num1 + num2


def fu(x, y):
    return x - y


fufu = Decorator(fu)
print(fufu(62, 7))

print(add_nums(3, 5))

newfun = Decorator(add_nums)
print(newfun(4, 2))
from time import time

print(time())
start = time()
for i in range(10000000):
    a = i ** 2
end = time()
print(end-start)