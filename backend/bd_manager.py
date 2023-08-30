import sqlite3

# Загрузка клиента при регистрации
def load_client_to_bd(user_data):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    insert_query = '''
        INSERT INTO Users (id, password, last_name, first_name, middle_name, email, company, phone)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''

    user_values = (
        user_data.id,
        user_data.password,
        user_data.last_name,
        user_data.first_name,
        user_data.middle_name,
        user_data.email,
        user_data.company,
        user_data.phone
    )

    cursor.execute(insert_query, user_values)
    connection.commit()

    connection.close()

def is_exist_user(user_data):
    # Проверка на существование пользователя по email
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE email = ?', (user_data.email,))
    existing_user = cursor.fetchone()
    conn.close()

    if existing_user:
        return True
    else:
        return False
    
def show_users():
    # Соединение с базой данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Выполнение SQL-запроса
    cursor.execute('SELECT * FROM Users')

    # Получение результатов запроса
    rows = cursor.fetchall()

    # Закрытие соединения с базой данных
    conn.close()

    # Вывод результатов
    for row in rows:
        print(row)
