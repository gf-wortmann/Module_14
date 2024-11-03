# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."
# Цель: освоить основные команды языка SQL и использовать их в коде используя SQLite3.

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
''')

connection.commit()

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)"
                   , (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))
connection.commit()

for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))
    # print(i)
connection.commit()

for i in range(1, 11, 3):
    # print(i)
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))
connection.commit()

cursor.execute("SELECT * FROM Users WHERE age <> ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]}|Почта: {user[2]}|Возраст: {user[3]}|Баланс: {user[4]}')

connection.close()
