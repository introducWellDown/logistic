from pydantic import BaseModel
import random
import sqlite3

# Модель данных для запроса
class UserData(BaseModel):
    ID:str
    password: str
    last_name: str
    first_name: str
    middle_name: str
    email: str
    company: str
    phone: str    

def generate_id():
    seed = list("123456789123456789123456789123456789123456789")
    random.shuffle(seed)
    id = str(''.join([random.choice(seed) for x in range(6)]))
    return id

def generate_password():
    seed = list("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
    random.shuffle(seed)
    password = str(''.join([random.choice(seed) for x in range(6)]))
    return password

def is_uniq_id(userID,nameDB):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    while True:
        cursor.execute(f'SELECT id FROM {nameDB} WHERE id = ?', (userID,))
        row = cursor.fetchone()

        if row is None:
            db.close()
            return userID, True
        else:
            userID = generate_id()

    