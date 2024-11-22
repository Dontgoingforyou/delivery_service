# Delivery Service API

API для управления заявками службы доставки. Поддерживает создание заявок, получение информации о заявке, изменение статуса и удаление заявок (при условии, что заявка не была передана в доставку).

## Функциональность

- Создание заявки: POST **/api/orders/**
- Получение информации о заявке: GET **/api/orders/{id}/**
- Изменение статуса заявки: POST **/api/orders/{id}/set_status/**
- Удаление заявки: DELETE **/api/orders/{id}/** (только для заявок в статусе **created**)

## Стек технологий

- Python 3.12
- Django 5.1.3
- Django REST Framework
- PostgreSQL
- Docker и Docker Compose (для работы с базой данных)

## Установка и запуск

1. Установка зависимостей

- Склонируйте репозиторий:
     ```bash
     git clone https://github.com/Dontgoingforyou/delivery_service.git
     cd delivery_service
      
- Установите зависимости:
    ```bash
    poetry install

- Активируйте виртуальное окружение:
    ```bash
    poetry shell

2. Настройка базы данных

Используйте Docker для развертывания PostgreSQL:

- Запустите контейнер PostgreSQL:
     ```bash
     docker compose up -d

Контейнер настроен на использование следующих параметров:
- Имя базы данных: delivery
- Пользователь: postgres
- Пароль: evibul29
- Порт: 5432

3. Настройка .env файла
Переименуйте .env.sample в .env и заполните пустые поля данными:
    ```bash
    DB_NAME=delivery
    DB_USER=postgres
    DB_PASSWORD=evibul29
    DB_HOST=localhost
    DB_PORT=5432

4. Применение миграций
    ```bash
    python manage.py makemigrations
    python manage.py migrate
   
5. Запуск сервера
    ```bash
   python manage.py runserver

Приложение будет доступно по адресу: http://127.0.0.1:8000/.

## Тестирование API

Примеры запросов

1. Создание заявки
- URL: POST **/api/orders/**
- Тело запроса:
    ```bash
    {
    "name": "Посылка",
    "description": "Товар для доставки"
    }
  
2. Получение информации о заявке
- URL: GET **/api/orders/{id}/**

3. Изменение статуса заявки
- URL: POST **/api/orders/{id}/set_status/**
- Тело запроса:
    ```bash
    {
    "status": "in_delivery"
    }
  
4. Удаление заявки
- URL: DELETE **/api/orders/{id}/**
