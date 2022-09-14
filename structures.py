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
            popping = self.__data.pop(self.__top - 1)
            self.__top -= 1
            return popping
        else:
            print('пусто/empty')
            return None

    def get_size(self):
        return self.__size

    def get_top(self):
        return self.__top


class Queue:
    __data = list()
    __size = 0
    __capacity = 0

    def __init__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity

    def add(self, element: any):
        if self.__size < self.__capacity:
            self.__data.append(element)
            self.__size += 1
        else:
            print('переполнение/overflow')

    def pop(self):
        if self.__size > 0:
            popping = self.__data.pop(0)
            self.__size -= 1
            return popping
        else:
            print('пусто/empty')
            return None

    def get_capacity(self):
        return self.__capacity

    def get_size(self):
        return self.__size


class Queue_ring:
    __data = list()
    __size = 0
    __capacity = 0

    def __init__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity

    def add(self, element: any):
        if self.__size < self.__capacity:
            self.__data.append(element)
            self.__size += 1
        else:
            print('переполнение/overflow')

    def pop(self):
        if self.__size > 0:
            popping = self.__data.pop(0)
            # выдавливаемый элемент добавляется в хвост очереди-
            self.add(popping)
            return popping
        else:
            print('пусто/empty')
            return None

    def get_capacity(self):
        return self.__capacity

    def get_size(self):
        return self.__size


class Queue_priority:
    __data = list()
    __priority = list()
    __size = 0
    __capacity = 0

    def __init__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity

    def add(self, element: any, priority: int):
        if self.__size < self.__capacity:
            self.__data.append(element)
            self.__priority.append(priority)
            self.__size += 1
        else:
            print('переполнение/overflow')
    # при выдавливании берется элемент с самым высоким приоритетом
    def pop(self):
        if self.__size > 0:
            # ищем максимальное значение приоритета
            max_priority = max(self.__priority)
            # ищем индекс максимального значения приоритета
            index_max_priority = self.__priority.index(max_priority)
            # выдавливаем элемент с найденым индеском
            popping = self.__data.pop(index_max_priority)
            # удаляем приоритет из списка
            self.__priority.pop(index_max_priority)
            self.__size -= 1
            return popping
        else:
            print('пусто/empty')
            return None

    def get_capacity(self):
        return self.__capacity

    def get_size(self):
        return self.__size
