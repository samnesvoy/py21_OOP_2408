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
# with open('serialize.txt', 'w') as file:
#     json.dump(di, file,indent=2)

with open('serialize.txt','r') as file:
    dd=json.load(file)

print(type(dd))


