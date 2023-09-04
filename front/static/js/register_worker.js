const backButton = document.getElementById('back-link');
backButton.addEventListener('click', () => {
        window.location.href = '/registration-choice';
    
});


// Получение ссылки на форму регистрации
const registrationForm = document.getElementById('registration-form');
const successMessage = document.querySelector('.center-content');

// Функция, которая будет вызываться при отправке формы
function registerWorker(event) {
    event.preventDefault();

    const lastName = document.getElementById('last_name').value;
    const firstName = document.getElementById('first_name').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;
    const company = document.getElementById('accountType').value;
    const company_code = document.getElementById('companyCode').value;

    const userData = {
        last_name: String(lastName), // Преобразование в строку
        first_name: String(firstName), // Преобразование в строку
        phone: String(phone), // Преобразование в строку
        email: String(email), // Преобразование в строку
        company: String(company), // Преобразование в строку
        company_code: String(company_code) // Преобразование в строку
    };

    fetch('/register-worker-successful', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
        registrationForm.style.display = 'none';
        // Переопределение ссылки для успешного статуса
        backButton.addEventListener('click', () => {
            window.location.href = '/';
        });
        // Показать блок с успешным сообщением
        showContainer()
        // Заполнить ID и пароль пользователя
        document.getElementById('worker-id').textContent = data.id; // Замените на актуальный ключ в объекте data
        document.getElementById('worker-password').textContent = data.password; // Замените на актуальный ключ в объекте data
        } else if (data.status === "error") {
            // Отображение окошка с сообщением об ошибке
            showError();
        } else if (data.status === "error_none_company_code"){
            // Отображение окошка с сообщением об ошибке
            showErrorNoneCode();
        }
    });

}


// Отображение контейнера
function showContainer() {
    successMessage.classList.remove('hidden');
}

// Скрытие контейнера
function hideContainer() {
    successMessage.classList.add('hidden');
}

function showError() {
    const notification = document.getElementById('email-exist-error');
    notification.style.display = 'block'; // Показываем элемент
    notification.style.opacity = '1'; // Устанавливаем полную прозрачность

    setTimeout(() => {
        notification.style.opacity = '0'; // Устанавливаем прозрачность 0 через 5 секунд
    }, 2000); // 5000 миллисекунд = 5 секунд
}

function showErrorNoneCode() {
    const notification = document.getElementById('code-none-error');
    notification.style.display = 'block'; // Показываем элемент
    notification.style.opacity = '1'; // Устанавливаем полную прозрачность

    setTimeout(() => {
        notification.style.opacity = '0'; // Устанавливаем прозрачность 0 через 5 секунд
    }, 2000); // 5000 миллисекунд = 5 секунд
}


// Привязка функции к событию отправки формы
registrationForm.addEventListener('submit', registerWorker);