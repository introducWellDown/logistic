import json
from fastapi.testclient import TestClient
from routing import app  # Импортируйте ваш экземпляр FastAPI приложения

client = TestClient(app)

def test_register_user_unprocessable_entity():
    # Подготовка данных для отправки
    invalid_data = {
        "id": "0",
        "password": "0",
        "last_name": "Smith",
        "first_name": "John",
        "middle_name": "middleName",
        "email": "email@mail.ru",
        "company": "company 1",
        "phone": "89998889922"
    }

    # Отправка POST-запроса на /register-user-successful
    response = client.post("/register-user-successful")

    # Проверка, что ответ сервера содержит код 422
    print(response.status_code )

test_register_user_unprocessable_entity()

