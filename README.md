# Менеджер паролей

## Автор
Корчагов Михаил

## Описание
Консольное приложение для безопасного хранения и управления паролями.

## Структура 
Password-Manager/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   └── password_record.py
│
├── views/
│   ├── __init__.py
│   └── console_view.py
│
├── controllers/
│   ├── __init__.py
│   └── password_controller.py
│
├── utils/
│   ├── __init__.py
│   └── password_generator.py
│
├── tests/
│   ├── __init__.py
│   └── test_app.py
│
├── data/
│   └── passwords.json
│
├── .gitignore
└── README.md

## Функционал
- Добавление паролей с валидацией
- Просмотр всех паролей
- Удаление паролей
- Генерация случайных паролей (4-50 символов)
- Поиск по названию сервиса
- Сохранение/загрузка в JSON

## Запуск

```bash
python main.py
