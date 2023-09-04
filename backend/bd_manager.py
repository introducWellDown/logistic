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

# Загрузка исполнителя при регистрации
def load_worker_to_bd(worker_data):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    insert_query = '''
        INSERT INTO Worker (id, password, last_name, first_name, phone, email, company, company_code)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''
    user_values = (
        worker_data.id,
        worker_data.password,
        worker_data.last_name,
        worker_data.first_name,
        worker_data.phone,
        worker_data.email,
        worker_data.company,
        worker_data.company_code
    )

    cursor.execute(insert_query, user_values)
    connection.commit()

    connection.close()

def is_exist(structure,table):
    # Проверка на существование пользователя по email
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {str(table)} WHERE email = ?', (structure.email,))
    existing_user = cursor.fetchone()
    conn.close()

    if existing_user:
        return True
    else:
        return False
    
def is_exist_company_code(structure):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Выполняем запрос к базе данных, чтобы найти запись с указанным name и code
        cursor.execute("SELECT * FROM Companies WHERE name = ? AND code = ?", (structure.company, structure.company_code))
        
        existing_company = cursor.fetchone()
        
        conn.close()
        
        if existing_company:
            return True  # Запись с таким name и code найдена
        else:
            return False  # Запись не найдена
    except sqlite3.Error as e:
        print(f"Ошибка при проверке компании и кода: {e}")
        return False  # В случае ошибки также возвращаем False
           
    
def show_pleer_bd(pleer):
    # Соединение с базой данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Выполнение SQL-запроса
    cursor.execute(f'SELECT * FROM {str(pleer)}')

    # Получение результатов запроса
    rows = cursor.fetchall()

    # Закрытие соединения с базой данных
    conn.close()

    # Вывод результатов
    for row in rows:
        print(row)
        
def add_company_with_code(name, code):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Вставляем запись в таблицу Companies
        cursor.execute("INSERT INTO Companies (name, code) VALUES (?, ?)", (name, code))
        
        conn.commit()
        conn.close()
        print(f"Компания '{name}' с кодом '{code}' успешно добавлена.")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении компании: {e}")
