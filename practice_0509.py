# class Test:
#     def __init__(self):
#         self.i = 5
#         self.f = 3.5
#
#     def __int__(self):
#         return self.i
#
#     def __float__(self):
#         return self.f
#
#
# t = Test()
#
# print(int(t))
# print(float(t))

class Person:
    __firstname = str()
    __lastname = str()
    __phone = str()
    __person_type = None

    def __init__(self, firstname: str, lastname: str, phone: str):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_phone(phone)

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_phone(self):
        return self.__phone

    def set_firstname(self, firstname: str):
        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname: str):
        self.__lastname = lastname.capitalize()

    def set_phone(self, phone: str):
        self.__phone = phone

    def set_firstname_godmode(self, firstname: str):
        self.__firstname = firstname

    def set_person_type(self, person_type: str):
        self.__person_type = person_type

    def get_person_type(self):
        return self.__person_type

    def __str__(self):
        return f'{self.__firstname} {self.__lastname} {self.__phone}'

    def to_file(self, filename: str):
        with open(filename, 'a') as file:
            file.write(f'{self.__person_type} {self.__str__()}\n')

    # @staticmethod
    # def from_file(filename: str):
    #     li=[]
    #     with open(filename, 'r') as file:
    #         persons = file.readlines()
    #         for person in persons:
    #             if person[0]=='student':
    #                 li.append()
    #         return Person(res[0], res[1], res[2])
    # self.set_firstname(res[0])
    # self.set_lastname(res[1])
    # self.set_phone(res[2])


class Student(Person):
    __group = str()

    def __init__(self, firstname: str, lastname: str, phone: str, group: str):
        super().__init__(firstname, lastname, phone)
        self.set_group(group)
        super().set_person_type('student')

    def get_group(self):
        return self.__group

    def set_group(self, group: str):
        self.__group = group

    def __str__(self):
        return f'{super().__str__()} {self.__group}'

    def from_file(self, filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_group(res[3])


class Teacher(Person):
    __subject = str()

    def __init__(self, firstname: str, lastname: str, phone: str, subject: str):
        super().__init__(firstname, lastname, phone)
        self.set_subject(subject)
        super().set_person_type('teacher')

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject: str):
        self.__subject = subject

    def __str__(self):
        return f'{super().__str__()} {self.__subject}'

    def from_file(self, filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_subject(res[3])


# li = []
# li.append(Student('Ivasyk', 'Bulkin', 'trinolyatrulyalya', 'Python11'))
# li.append(Student('Grigoiy', 'Terkin', '+387415874165', 'Python21'))
# li.append(Student('Anna', 'Chechetkina', '+04478451235', 'C++14'))
# li.append(Teacher('Tatyana', 'Stepanovna', 'phone_number', 'C++'))
# li.append(Student('Svetlana', 'Bulkina', 'trinolyatrulyalya2', 'Python11'))
# li.append(Student('Anatloiy', 'Fedorov', '0991234756', 'C++17'))

# for i in li:
#     i.to_file('test.txt')

class Group:
    __name = str()
    __li = list()

    def __init__(self, name: str):
        self.set_name(name)

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def append(self, person: Person):
        self.__li.append(person)

    def li_from_file(self, filename: str = 'test.txt'):
        with open(filename, 'r') as file:
            persons = file.readlines()
            for person in persons:
                person = person.split()
                if person[0] == 'student':
                    self.__li.append(Student(person[1], person[2], person[3], person[4]))
                if person[0] == 'teacher':
                    self.__li.append(Teacher(person[1], person[2], person[3], person[4]))

# li = li_from_file('test.txt')

# for i in li:
#     print(i)
# li_from_file()
# li[0].to_file('test.txt')
#
# li[0].from_file('test.txt')
