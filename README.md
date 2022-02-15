# Куда пойти — Москва глазами Артёма
Сайт доступен по [ссылке](https://itcosplay.pythonanywhere.com/).


## Необходимое окружение
|переменная|описание|тип|значение по умолчанию
|----------|--------|--------------|---------------------
|`SECRET_KEY`|Секретный ключ проекта|string|`empty`
|`DEBUG`|Отладочный режим|bool|`False`
|`ALLOWED_HOSTS`|см. [документацию](https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts)|string|`[]`
|`SECURE_SSL_REDIRECT`|см. [документацию](https://docs.djangoproject.com/en/4.0/ref/settings/#secure-ssl-redirect)|bool|`not DEBUG`
|`SECURE_HSTS_SECONDS`|см. [документацию](https://docs.djangoproject.com/en/4.0/ref/settings/#secure-hsts-seconds)|integer|`0`
|`SESSION_COOKIE_SECURE`|см. [документацию](https://docs.djangoproject.com/en/4.0/ref/settings/#session-cookie-secure)|bool|`not DEBUG`
|`CSRF_COOKIE_SECURE`|см. [документацию](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-cookie-secure)|bool|`not DEBUG`

Все переменные окружения должны храниться в файле .env в корне проекта.



## Как установить
* Клонируем репозиторий
* Добавляем файл .env с необходимыми переменными
* Создаем виртуальное окружение
* Устанавливаем зависимости
```
pip install -r requirements.txt
```


## Настройка
* Выполняем миграции
```
python manage.py migrate
```
* Содаем суперпользователя
```
python manage.py createsuperuser
```


## Использование
* Добавляем данные через админ панель
* Добавляем данные с помощью скрипта
```
python manage.py load_place <link>
```
Данные для сайта доступны по [ссылке](https://github.com/devmanorg/where-to-go-places/tree/master/places)
Необходимо копировать ссылку из кнопки raw.


## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

