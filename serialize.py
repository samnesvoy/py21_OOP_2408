import json

# di = {
#     'name': 'Vasiliy',
#     'id': 17,
#     'children': [
#         'Katrina',
#         'Zigfrid',
#     ],
#     'parents': {
#         'mother': 'Antonina',
#         'father': 'Julia',
#     },
#     'age': 43,
# }
# serialize_string = json.dumps(di)
#
# print(serialize_string)
# print(di)
#
di=(567,)
with open('serialize.txt', 'w') as file:
    json.dump(di, file,indent=2)

with open('serialize.txt','r') as file:
    dd=json.load(file)

print(type(dd))
# dumps - сериализация в строку
# dump - сериализация в файл
# loads - десериализация из строки
# load - десериализация из файла
# https://pythonworld.ru/moduli/modul-json.html
# https://pythonworld.ru/moduli/modul-pickle.html



