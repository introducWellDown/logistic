const backButton = document.getElementById('back-link');
backButton.addEventListener('click', () => {
    window.location.href = '/registration-choice';
});

// Получение ссылки на форму регистрации
const registrationForm = document.getElementById('registration-form');

// Функция, которая будет вызываться при отправке формы
function registerUser(event) {
    event.preventDefault();

    const lastName = document.getElementById('last_name').value;
    const firstName = document.getElementById('first_name').value;
    const middleName = document.getElementById('second_name').value;
    const email = document.getElementById('email').value;
    const company = document.getElementById('accountType').value;
    const phone = document.getElementById('phone').value;

    const userData = {
        id: "0", // Это уже строка, так что преобразование не требуется
        password: "0", // То же самое здесь
        last_name: String(lastName), // Преобразование в строку
        first_name: String(firstName), // Преобразование в строку
        middle_name: String(middleName), // Преобразование в строку
        email: String(email), // Преобразование в строку
        company: String(company), // Преобразование в строку
        phone: String(phone) // Преобразование в строку
    };

    fetch('/register-user-successful', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // Вывод сообщения об успешной регистрации
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}

// Привязка функции к событию отправки формы
registrationForm.addEventListener('submit', registerUser);
