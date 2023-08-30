import sqlite3

# Создание подключения к базе данных (если базы данных нет, она будет создана)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблицы Companies
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Companies (
        code TEXT ,
        name TEXT
    )
''')

# Создание таблицы Users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER,
        password TEXT,
        last_name TEXT,
        first_name TEXT,
        middle_name TEXT,
        email TEXT,
        company TEXT,    
        phone TEXT
    )
''')

# Создание таблицы Performers
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Performers (
        id TEXT,
        last_name TEXT,
        first_name TEXT,
        email TEXT,
        company TEXT,
        company_code TEXT REFERENCES Companies(code)
    )
''')

# Создание таблицы Orders
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        id TEXT,
        user_id INTEGER REFERENCES Users(id),
        sender_city TEXT,
        receiver_city TEXT,
        delivery_method TEXT,
        weight REAL,
        material TEXT,
        send_date TEXT,
        calculated INTEGER,
        calculated_status INTEGER,
        price REAL,
        performer_id INTEGER REFERENCES Performers(id)
    )
''')

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()
