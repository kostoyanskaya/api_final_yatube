# Проект «API для Yatube»
Yatube API - это  платформа для блогов, которая предлагает широкий спектр инструментов для создания, редактирования и удаления собственных публикаций и комментариев. Она также предоставляет возможность регистрации новых пользователей, подписки на интересующие блоги и отслеживания активности других участников сообщества.

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

## Пример запроса:
```
/api/v1/posts/
```

## Документация:
[Documentation](http://127.0.0.1:8000/redoc/)
***

## Автор
#### [Анастасия](https://github.com/kostoyanskaya/)