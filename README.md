# Проект «API для Yatube»
Yatube API - это  платформа для блогов, которая предлагает широкий спектр инструментов для создания, редактирования и удаления собственных публикаций и комментариев. Она также предоставляет возможность регистрации новых пользователей, подписки на интересующие блоги и отслеживания активности других участников сообщества.

## Используемые технологии

В проекте используются следующие технологии и библиотеки:

- **Django** - веб-фреймворк для создания веб-приложений.
- **Django REST Framework** - библиотека для создания API на Django.
- **Djoser** - библиотека для упрощения работы с пользователями и аутентификацией.
- **pytest** - фреймворк для тестирования.
- **Pillow** - библиотека для работы с изображениями.
- **Requests** - библиотека для работы с HTTP-запросами.
- **django-filter** - библиотека для фильтрации данных в Django.
- **PyJWT** - библиотека для работы с JWT.

## Установка

1. Клонировать репозиторий:

    ```python
    git clone git@github.com:kostoyanskaya/api_final_yatube.git
    ```

2. Перейти в папку с проектом:

    ```python
    cd yatube_api
    ```

3. Установить виртуальное окружение для проекта:

    ```python
    python -m venv venv
    ```

4. Активировать виртуальное окружение для проекта:

    ```python
    # для OS Lunix и MacOS
    source venv/bin/activate

    # для OS Windows
    source venv/Scripts/activate
    ```


5. Установить зависимости:

    ```python
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

6. Выполнить миграции:

    ```python
    python manage.py migrate
    ```

7. Запустить проект:
   ```python
    python manage.py runserver
    ```

## Пример запроса и ответа

### POST запрос
`/api/v1/posts/`

body:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2024-09-01T17:57:45.389Z",
  "image": "string",
  "group": 0
}
```


## Документация:
[Documentation](http://127.0.0.1:8000/redoc/)
***

## Автор
#### [Виктория](https://github.com/kostoyanskaya/)
