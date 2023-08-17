import sqlite3
from logic import UserData

# Загрузка клиента при регистрации
def load_client_to_bd(user_data: UserData):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        query = '''
            INSERT INTO Users (id,password,last_name, first_name, middle_name, email, company, phone)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        values = (user_data.ID,user_data.password,user_data.last_name, user_data.first_name, user_data.middle_name, user_data.email,user_data.company, user_data.phone)
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def load_worker_to_bd(user_data: UserData):
    
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Вставка данных в таблицу Users
    query = '''
        INSERT INTO Users (id,password,last_name, first_name, middle_name, email, company, phone)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''
    values = (user_data.ID,user_data.password,user_data.last_name, user_data.first_name, user_data.middle_name, user_data.email,user_data.company, user_data.phone)
    cursor.execute(query, values)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()