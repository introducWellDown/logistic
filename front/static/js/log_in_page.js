const registerButton = document.getElementById('register-button');
registerButton.addEventListener('click', () => {
    window.location.href = '/registration-choice';
});

const loginForm = document.querySelector('form'); // Получить форму
const loginButton = document.getElementById('login-button');

// Функция, которая будет вызываться при отправке формы
function loginUser(event) {
    event.preventDefault();

    const id = document.getElementById('id').value;
    const password = document.getElementById('password').value;

    const userLoginData = {
        id: id, 
        password: String(password) // Преобразование в строку
    };

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userLoginData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success" && data.person === "Worker") {
            window.location.href = '/worker-main-page';
        }else if (data.status === "success" && data.person === "Client") {
            window.location.href = '/client-main-page';
        }else if (data.status === "logining_error") {
            // Отображение окошка с сообщением об ошибке
            showLoginError();
        }
    });

}


function showLoginError() {
    const notification = document.getElementById('login-error');
    notification.style.display = 'block'; // Показываем элемент
    notification.style.opacity = '1'; // Устанавливаем полную прозрачность

    setTimeout(() => {
        notification.style.opacity = '0'; // Устанавливаем прозрачность 0 через 5 секунд
    }, 2000); // 5000 миллисекунд = 5 секунд
}



// Привязка функции к событию отправки формы
loginForm.addEventListener('submit', loginUser); // Навесить обработчик на форму

