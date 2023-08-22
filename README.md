# Это проект по автоматизации Swag Labs


## Цели
- Повышение скорости тестирования и снижение ручных усилий
- Снизить общую стоимость тестирования
- Проверка корректности бизнес-логики приложения

## Структура проекта
Проект написан в стиле Page Object Model:
- Все методы действия и проверки выделены в отдельные методы в классах PageObject; 
- Все необходимые селекторы лежат только в теле конкретного класса;
- Нет assert в теле тестов.

Также в проекте добавлено логгирование и отчетность allure 

Во время написания проекта старался придерживаться читаемого кода, правильных коммитов и в целом логики. 

## Как запустить проект?

### Копирование репозитория
```
git clone https://github.com/sadpatheticboy/qa_shop_project.git
cd qa_shop_project
```

### Установка требуемых пакетов
```
pip install -r requirements.txt 
```

### Запуск необходимых тестов
```
pytest -s -v
```