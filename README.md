### Foodgram - социальная сеть о кулинарии
ДИПЛОМНАЯ РАБОТА

![workflow status](https://github.com/admi20/foodgram-project-react/actions/workflows/yamdb_workflow.yml/badge.svg)

[Проверьте работоспособность приложения](http://localhost/admin/)


#### Описание

Проект Foodgram позволяет пользователям делитесь своими рецептами и взаимодействовать с рецептами других пользователей. Рецепты можно найти по тегам, ингридиентам.

#### Установка

Клонировать репозиторий приложения:

```
git clone https://github.com/admi20/foodgram-project-react.git
```

Перейти в корневой каталог:

```
cd foodgram-project-react
```

Создать виртуальное окружение:

```
python -m venv venv
```

Активировать виртуальное окружение:

- Linux/macOS

```
source venv/bin/activate
```

-Windows

```
source venv/scripts/activate
```

Обновить pip:

```
python -m -pip install --upgrade pip
```

Установить зависимость из файла requirements.txt:

```
pip install -r requirements.txt
```

Произвести миграции:

```
python manage.py migrate
```

Импортировать тестовые данные в базу данных:

```
python manage.py import_csv_data
```

Запустить проект:

```
python manage.py runserver
```

#### Шаблон файла .env

DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql\
DB_NAME=postgres # имя базы данных\
POSTGRES_USER=postgres # логин для подключения к базе данных\
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)\
DB_HOST=db # название сервиса (контейнера)\
DB_PORT=5432 # порт для подключения к БД

#### Команда разработчиков

Dmitry Parkhomenko, Petr Shopin, Dmitrii Abashkin
