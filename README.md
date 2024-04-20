# UTF.tech_Test
## Как запустить проект:

Клонировать репозиторий на Windows и перейти в него в командной строке:

```
git clone git@github.com:Gordey3000/UTF.tech_Test.git

```

```
cd UTF.tech_Test
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py makemigrations
python manage.py migrate
```

Заполнить БД:
```
python manage.py loaddata foods.json
```

Запустить проект:

```
python manage.py runserver
```
## Примеры запросов.

GET /api/v1/foods/ - получение списка всех блюд.

GET /api/v1/foods/1/ - получение блюда с code 1.