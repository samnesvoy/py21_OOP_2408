import sqlite3


# создание таблицы
def create_users():
    # подключение к базе
    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    # выполнение запроса
    cursor.execute(
        # CREATE - ключевое слово для создания
        'CREATE TABLE IF NOT EXISTS users('
        'name text, '  # колонки таблицы состоят из имени и типа данных
        'phone text,'
        ')'
    )
    connect.commit()


# создание таблицы на основании входящих данных
def create_smth_smart(table: str, data: dict):
    keys = list(data.keys())
    values = list(data.values())
    req = f'CREATE TABLE IF NOT EXISTS {table}('

    for i in range(len(keys)):
        req += f'{keys[i]} {values[i]}, '
    req = req[:-2] + ')'
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
    # WHERE(где) имя_колонки=значение (необязательный элемент
    get = f'SELECT name, phone FROM users WHERE name="{name}"'
    cursor.execute(get)
    # метод fetchall возвращает список кортежей с заданными значениями
    result = cursor.fetchall()
    print(result)


# get_users('*')


# us = {'name': 'Petya', 'phone': '123456'}
# add_user(us)
# create_smth_smart('table_name', {'na': 'text', 'qw': 'text', 'asd': 'text', 'xc': 'text', 'qq': 'text'})

# Day 2
# удаление таблицы
def delete_table(name: str):
    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    req = f'DROP TABLE IF EXISTS {name}'
    cursor.execute(req)
    connect.commit()


# delete_table('types')

# типы данных хранимые в базе
create_smth_smart('types',
                  {
                      'string': 'text',
                      'number': 'int',
                      'float': 'real',
                      'void': 'NULL',
                      'binary': 'blob'
                  }
                  )

# дополнительные параметры строк при создании таблицы
create_smth_smart(table='products', data={
    'name': 'text not null',
    'description': 'text',
    'price': 'real default 0.0',
    'id': 'integer primary key autoincrement'
}
                  )


def add_smth_to_sometable(table: str, data: dict):
    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    columns = ''
    values = ''
    for i in range(len(data.keys())):
        columns += f'{list(data.keys())[i]}, '
        values += f'"{list(data.values())[i]}", '
    columns = columns[:-2]
    values = values[:-2]

    request_in_smth = f'INSERT INTO {table}' \
                      f' ({columns}) ' \
                      f'VALUES ' \
                      f'({values});'
    print(request_in_smth)
    cursor.execute(request_in_smth)
    connect.commit()


# add_smth_to_sometable(table='products',
#                       data={
#                           'name': 'еда',
#                           'description': 'очень вкусная',
#                           'price': 321.12,
#
#                       })

create_smth_smart(table='reviews',
                  data={
                      'id': 'integer primary key autoincrement',
                      'user_name': 'text not null',
                      'product_id': 'integer',
                      'review': 'text',
                      'foreign key (user_name)': 'references users (name)',
                      'foreign key (product_id)': 'references products (id) ON DELETE CASCADE'
                  })

add_smth_to_sometable(table='reviews',
                      data={
                          'review': 'какая прекрасная игра',
                          'user_name': 'Alla',
                          'product_id': 6,

                      })


def drop_smth(table: str, smth_id: int):
    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    req = f'DELETE FROM {table} WHERE id={smth_id};'
    cursor.execute(req)
    connect.commit()


drop_smth(table='products', smth_id=6)


def exist_smth(table: str, column: str, column_value: str):
    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    req = f'SELECT EXISTS (SELECT {column} FROM {table} WHERE {column}="{column_value}") AS {column};'
    cursor.execute(req)
    print(cursor.fetchall())
    connect.commit()


exist_smth(table='products', column='id', column_value='2')
