# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"
# Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи.

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute("DELETE FROM Users WHERE id =?", (6,))
connection.commit()

cursor.execute("SELECT COUNT(*) FROM Users")
users_count = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
total_balances = cursor.fetchone()[0]

print(f'Средний баланс: {total_balances / users_count}')
