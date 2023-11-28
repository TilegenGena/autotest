// Получаем элементы DOM
const countElement = document.getElementById("count");
const incrementButton = document.getElementById("increment");
const decrementButton = document.getElementById("decrement");

// Инициализируем счетчик
let count = 0;

// Функция для обновления счетчика и отображения его значения
function updateCount() {
    countElement.textContent = count;
}

// Обработчик события для кнопки "Увеличить"
incrementButton.addEventListener("click", function () {
    count++;
    updateCount();
});

// Обработчик события для кнопки "Уменьшить"
decrementButton.addEventListener("click", function () {
    count--;
    updateCount();
});

// Инициализация счетчика при загрузке страницы
updateCount();


function showAlert() {
    var textValue = document.getElementById("textInput").value;
    alert(textValue);
}