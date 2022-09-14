# stack

class Stack:
    __data = list()
    __top = 0
    __size = 0

    def __init__(self, size: int):
        if size > 0:
            self.__size = size

    def add(self, element: any):
        if self.__top < self.__size:
            self.__data.append(element)
            self.__top += 1
        else:
            print('переполнение/overflow')

    def pop(self):
        if self.__top > 0:
            popping = self.__data.pop(self.__top)
            self.__top -= 1
            return popping
        else:
            print('пусто/empty')
            return None

    def get_size(self):
        return self.__size

    def get_top(self):
        return self.__top
