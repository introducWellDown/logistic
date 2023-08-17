const choiceButton_1 = document.getElementById('choice-button-1');
choiceButton_1.addEventListener('click', () => {
    window.location.href = '/register-worker';
});

const choiceButton_2 = document.getElementById('choice-button-2');
choiceButton_2.addEventListener('click', () => {
    window.location.href = '/register-client';
});

const backButton = document.getElementById('back-link');
backButton.addEventListener('click', () => {
    window.location.href = '/';
});