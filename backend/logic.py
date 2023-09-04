import pydantic as pd
import random


# Модель данных для запроса
class UserData(pd.BaseModel):
    last_name: str
    first_name: str
    middle_name: str
    email: pd.EmailStr
    company: str
    phone: str    

# Класс в котором будет уже все данные по заказчику
class FullUserData(UserData):
    id: int
    password: str

# Модель данных для запроса
class WorkerData(pd.BaseModel):
    last_name: str
    first_name: str
    phone: str
    email: pd.EmailStr
    company: str
    company_code: str
        

# Класс в котором будет уже все данные по Исполнителю
class FullWorkerData(WorkerData):
    id: int
    password: str



def generate_id():
    seed = list("123456789123456789123456789123456789123456789")
    random.shuffle(seed)
    id = str(''.join([random.choice(seed) for x in range(6)]))
    return int(id)

def generate_password():
    seed = list("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
    random.shuffle(seed)
    password = str(''.join([random.choice(seed) for x in range(6)]))
    return password


    