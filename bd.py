import sqlite3




# создание таблицы
def create_users():
    # подключение к базе
    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    # выполнение запроса
    cursor.execute(
        # CREATE - ключевое слово для создания
        'CREATE TABLE users('
                   'name text, '    # колонки таблицы состоят из имени и типа данных
                   'phone text,'
                   ')'
    )
    connect.commit()
# создание таблицы на основании входящих данных
def create_smth_smart(table: str, user: dict):
    keys = list(user.keys())
    values = list(user.values())
    req = f'CREATE TABLE {table}('

    for i in range(len(keys)):
        req += f'{keys[i]} {values[i]}, '
    req = req[:-3] + ')'
    print(req)

    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    cursor.execute(req)
    connect.commit()

# добавление данных в таблицу
def add_user(user: dict):
    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    print(list(user.keys())[0])
    print(user.values())
    # INSERT INTO(вставить в) имя_таблицы(названия колонок)
    # VALUES(значения) (перечисляются в круглых скобках через запятую) в конце точка с запятой
    request_in_users = f'INSERT INTO users' \       
                       f' (name, phone) ' \
                       f'VALUES ' \
                       f'("{user["name"]}", {str(user["phone"])});'
    print(request_in_users)
    cursor.execute(request_in_users)
    connect.commit()

# получение данных из таблицы
def get_users(name):
    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    # SELECT(выбрать) через запятую перечисляются имена колонок или ставится * (все колонки)
    # FROM(из) имя_таблицы
    #WHERE(где) имя_колонки=значение (необязательный элемент
    get = f'SELECT name, phone FROM users WHERE name="{name}"'
    cursor.execute(get)
    # метод fetchall возвращает список кортежей с заданными значениями
    result = cursor.fetchall()
    print(result)


get_users('Petya')

# us = {'name': 'Petya', 'phone': '123456'}
# add_user(us)
# create_smth_smart('table_name', {'na': 'text', 'qw': 'text', 'asd': 'text', 'xc': 'text', 'qq': 'text'})
