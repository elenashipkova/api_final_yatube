# Описание проекта
## Финальное API для учебного проекта мини-блога ___Yatube___

__Реализованный функционал:__
```
1. просмотр, создание, редактирование, удаление постов и комментариев к ним;
2. возможность подписки на авторов и получение списка подписчиков;
3. создание групп и получение их списка;

API доступно аутентифицированным пользователям. Аутентификация на основе JWT-токена.

<a name="redoc"></a>
Подробная документация доступна на основе [Redoc](http://localhost:8000/redoc/)
```
__Установка:__
```
Клонируйте репозиторий
    git clone https://github.com/elenashipkova/api_final_yatube.git

Разверните и активируйте виртуальное окружение
    python -m venv venv
    source venv/bin/activate

Примените зависимости
    pip install -r requirements.txt

Выполните миграции
    python manage.py makemigrations
    python manage.py migrate

Запустите сервер
    python manage.py runserver

```

__Примеры__

Получить токен 
    [метод POST на localhost:8000/api/v1/token/ ](localhost:8000/api/v1/token/ )
    {
        "username": "Testuser",
        "password": "Ydksls2!"
    }

При выполнении запросов к API токен передается в заголовке _Authorization: Bearer <токен>_

<!--more--> [Redoc](#redoc)
